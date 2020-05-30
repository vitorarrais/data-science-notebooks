import sys
# import libraries
import nltk
nltk.download(['punkt', 'wordnet', 'stopwords'])

import pandas as pd
import numpy as np
import re
import pickle
from sqlalchemy import create_engine
from nltk.tokenize import word_tokenize
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.svm import LinearSVC


def load_data(database_filepath):
    """
    Load data from sql database and split it into X, y and classes.
    """

    engine = create_engine(f'sqlite:///{database_filepath}')
    df = pd.read_sql_table('Messages', engine)
    X = df['message']
    y = df[df.columns.difference(['id','message', 'original', 'genre'])]

    categories = df.columns.difference(['id','message', 'original', 'genre']).values
    return X, y, categories

def tokenize(text):
    """
    Tokenize given text by applying various nlp algorithms. 
    """

    # normalize
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9]", " ", text) 

    # tokenize
    words = word_tokenize(text)

    # remove stop words
    words = [w for w in words if w not in stopwords.words("english")]
    
    # lemmatize
    words = [WordNetLemmatizer().lemmatize(word, pos='v') for word in words]

    return words


def build_model():
    """
    Returns a trained multi-label classifier model.
    """

    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])
    
    parameters = {
        'vect__ngram_range': ((1, 1), (1, 2)),
        'vect__max_df': (0.75, 1.0),
        'tfidf__use_idf': (True, False),
    }
    
    return GridSearchCV(pipeline, param_grid=parameters)


def display_results(cv, y_test, y_pred):
    """
    Print out a confusion matrix, accuracy and best parameters.
    """

    labels = np.unique(y_pred)
    confusion_mat = confusion_matrix(y_test, y_pred, labels=labels)
    accuracy = (y_pred == y_test).mean()

    print("Labels:", labels)
    print("Confusion Matrix:\n", confusion_mat)
    print("Accuracy:", accuracy)
    print("\nBest Parameters:", cv.best_params_)
    return accuracy


def evaluate_model(model, X_test, y_test, category_names):
    """
    Predict on a test data and display the results. 
    """

    # predict on test data
    y_pred = model.predict(X_test)
    y_columns = category_names
    df_y_pred = pd.DataFrame(y_pred, columns=y_columns)
    df_y_test = pd.DataFrame(y_test, columns=y_columns)

    # prints out report for each category
    report = {}
    for column in y_columns:
        report[column] = classification_report(df_y_test[column].values, df_y_pred[column].values)
        print(report[column])
    

def save_model(model, model_filepath):
    """
    Saves a model as a pickle file.
    """

    with open(model_filepath, 'wb') as pickle_file:
        pickle.dump(model, pickle_file)


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()