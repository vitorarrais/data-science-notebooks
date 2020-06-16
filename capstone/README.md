# Data Scientist Nanodegree Capstone Project

## Overview

In this project I built a recommendation model of offers for Starbucks customers.

## Components

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

Data sets are in the data folder.

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