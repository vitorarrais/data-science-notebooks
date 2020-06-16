# Data Scientist Nanodegree Capstone Project

## Overview

In this project I built a recommendation model of offers for Starbucks customers.

## Problem Statement

The problem is formulated around a recommendation problem, where Starbucks wants to find the best offers for its costumers. In Starbucks stand point, a good recommendation engine is desirable because it will avoid spamming offers to customer that won't buy them. Additionally, it increases the chance of tailoring good offers to customers with higher chances to buy them. That will potentially increase the offer conversion rate, and lead to a increase in sells too.

## Jupyter Notebook

`starbucks.ipynb`

## Dependencies 

```
import pandas as pd
import numpy as np
import math
import json
import random
import matplotlib.pyplot as plt
from datetime import date, datetime
```

## Running

Use the notebook to run in your local machine. You're going to need jupyter installed.

## Data Sets

Data sets are in the `data` folder.

The data is contained in three files:

* portfolio.json - containing offer ids and meta data about each offer (duration, type, etc.)
* profile.json - demographic data for each customer
* transcript.json - records for transactions, offers received, offers viewed, and offers completed

Here is the schema and explanation of each variable in the files:

**portfolio.json**
* id (string) - offer id
* offer_type (string) - type of offer ie BOGO, discount, informational
* difficulty (int) - minimum required spend to complete an offer
* reward (int) - reward given for completing an offer
* duration (int) - time for offer to be open, in days
* channels (list of strings)

**profile.json**
* age (int) - age of the customer 
* became_member_on (int) - date when customer created an app account
* gender (str) - gender of the customer (note some entries contain 'O' for other rather than M or F)
* id (str) - customer id
* income (float) - customer's income

**transcript.json**
* event (str) - record description (ie transaction, offer received, offer viewed, etc.)
* person (str) - customer id
* time (int) - time in hours since start of test. The data begins at time t=0
* value - (dict of strings) - either an offer id or transaction amount depending on the record

## Results

```
actual
[   nan  10.      nan    nan  10.      nan    nan   4.44  10.      nan]

predicted
[  8.54  11.27   3.91   5.04   9.38   8.64   9.99   4.5   10.35   8.07]
```

We can see that the predicted values are pretty close to the actual values. That makes us believe that the prediction for NaN values are accurate as well.

Finally, we need to decice which offers we're going to recommend to user 1500. Here, we will recommend offers where the journey's score is above the dataset mean (5.67).

To customer 1500, we recommend the following offers:  
```
['offer_0', 'offer_1', 'offer_4', 'offer_5', 'offer_6', 'offer_8', 'offer_9']
```
