import sys
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """
    Reads the specified csv files and merge them.
    """
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    return messages.merge(categories, on='id')


def clean_data(df):
    """
    Return a cleaned dataframe. 
    """
    # split categories into separate columns
    categories = pd.DataFrame(df['categories'].str.split(';', expand=True))
    # select the first row of the categories dataframe
    row = categories.iloc[0]

    # transform column names by deleting numrical posfix
    category_colnames = row.apply(lambda s: s[:-2])
    categories.columns = category_colnames

    # transform categories values into 0's and 1's
    for column in categories:
        series_as_string = categories[column].astype(str)
        # set each value to be the last character of the string
        categories[column] = series_as_string.str[-1:]

        # convert column from string to numeric
        categories[column] = categories[column].apply(lambda s: int(s))
        
    # drop the original categories column from `df`
    df =  df.drop(columns='categories')
    
    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df,categories], axis=1)

    # drop duplicates
    df = df.drop_duplicates()

    return df

def save_data(df, database_filename):
    """
    Save a dataframe to a sql database.
    """
    engine = create_engine(f'sqlite:///{database_filename}')
    df.to_sql('Messages', engine, index=False)


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()