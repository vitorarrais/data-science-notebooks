#!/bin/bash

DATES=(
    '2020-03-17'
    '2020-02-18'
    '2020-01-10'
    '2019-12-11'
    '2019-11-12'
    '2019-10-16'
    '2019-09-19'
    '2019-08-12'
    '2019-07-11'
    '2019-06-08'
    '2019-05-14'
    '2019-04-11'
    '2019-03-08'
    '2019-02-06'
    '2019-01-14'
    '2018-12-10'
    '2018-11-07'
    '2018-10-10'
    '2018-09-12'
    '2018-08-14'
    '2018-07-10'
    '2018-06-09'
    '2018-05-14'
    '2018-04-12'
    '2017-05-08'
    '2017-04-08'
    '2017-03-06'
    '2017-02-10'
    '2017-01-06'
    '2016-12-08'
    '2016-11-07'
    '2016-10-04'
    '2016-09-05'
    '2016-08-04'
    '2016-07-05'
    '2016-06-03'
    '2016-05-03'
    '2016-04-04'
    '2016-02-04'
    '2016-01-04'
    '2015-12-05'
    '2015-11-08'
    '2015-10-03'
)

for date in "${DATES[@]}"; do
    curl http://data.insideairbnb.com/germany/be/berlin/"$date"/data/listings.csv.gz --output listings_"$date".csv.gz
    gunzip listings_"$date".csv.gz
    curl http://data.insideairbnb.com/germany/be/berlin/"$date"/data/calendar.csv.gz --output calendar_"$date".csv.gz
    gunzip calendar_"$date".csv.gz
    curl http://data.insideairbnb.com/germany/be/berlin/"$date"/data/reviews.csv.gz --output reviews_"$date".csv.gz
    gunzip reviews_"$date".csv.gz
donegun