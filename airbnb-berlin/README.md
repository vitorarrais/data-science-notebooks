# AirBnb Berlin Dataset Analysis

## Content

* Listings, including full descriptions and average review score
* Reviews, including unique id for each reviewer and detailed comment
* Calendar, including listing id and the price and availability for that day

## Requirements

* python 3.6
* numpy
* pandas
* matplotlib
* seaborn

## Structure

* **download.sh** a bash script to download the .csv files
* **airbnb_berlin.ipynb** jupyter notebook used for the analysis

## Motivation

In this analisys I've used publicly available data from Airbnb listings in Berlin from 2015 to 2020 to answer following questions:
1. How does number of rooms influence review scoring and pricing ?
2. How do amenities impact in the review scoring ?
3. How did prices evolve over time?
4. How listings are spread within neighbourhoods ?
5. How prices vary by neighbourhood ?

## Findings

1. Number of rooms do not have relevant correlation with price and review score.
2. Offered amenities do not have relevant correlation with review score.
3. Prices are increasing each year, which can a be considered good news if you are a host. Fortunately though, prices increase slowly when compared to housing and renting indexes, which have had lots of speculation in recent years.
4. Neukolln is the neighbourhood with most listings. 
5. Avoid Wilmesdorf because is the most expensive neighbourhood by far. 

#### Bonus 
* Book in advance if you’re going to visit Berlin in the summer, AirBnB can be very competitive at this time. 
* In case you want plenty of diverse options like bars, restaurants and nightclubs, you should stay in Neukölln or Prenzlauer Berg.
* Lastly, a very sad story for AirBnB is the fact that COVID-19 has hit hard the platform early this year.

## Blog Post
* https://medium.com/@vitorarrais/how-to-get-the-most-of-airbnb-in-berlin-7543baf29b33

## Acknowledgment

The data publicly available at [InsideAirbnb](http://insideairbnb.com/berlin)
