# sqlalchemy-challenge
UNC_data_bootcamp_module_10

## Challenge Description
### Background
> Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

***from the UNC Bootcamp instructions for this challenge***

## Deliverables
This challenge consists of two parts. For Part-1 we'll use resource file data to create a __Jupyter notebook__ to calculate the precipitation and temperature in Hawaii within a given date range. Then for Part-2 we will use the data from that Jupyter notebook to create a __Flask API__ to output those statistics as JSON style webpages.

### Part-1: Analyze and Explore the Climate Data
For this part, we are using Python and SQLAlchemy to do a basic climate analysis in a Jupyter notebook called __climate_analysis_SDT.ipynb__ using SQLAlchemy (ORM queries), Pandas, and Matplotlib. We are using the provided starter code files (climate_starter.ipynb and hawaii.sqlite) along with the Resource folder files to analyze this data. When finished, we will use this data to perform a Precipitation analysis and as well as a Station analysis in two subsections and plot our findings on a chart. Chart data will be provided for each subsection.

#### Precipitation Analysis
This analysis is to be performed in the following steps per the instructions:
1) Find the most recent date in the dataset.

2) Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.

3) Select only the ___"date"___ and ___"prcp"___ values.

4) Load the query results into a Pandas DataFrame. Explicitly set the column names.

5) Sort the DataFrame values by "date".

6) Plot the results by using the DataFrame plot method:

_Hawaii Precipitation Chart_

![HI-prcp-chart](https://github.com/SteveTuttle/sqlalchemy-challenge/blob/main/Images/HI_prcp.png)

7) Use Pandas to print the summary statistics for the precipitation data.

#### Station Analysis
This analysis is to be performed in the following steps per the instructions:
1) Design a query to calculate the __total number of stations__ in the dataset.

2) Design a query to find the __most-active stations__, meaning:
* List the stations and observation counts in descending order.
* Determine which station id has the greatest number of observations.

3) Design a query that calculates the __lowest, highest, and average temperatures__ that filters on the __most-active station id__ found in the previous query.

4) Design a query to get the __previous 12 months of Temperature Observation (TOBS) data__ as follows:
* Filter by the station that has the greatest number of observations.
* Query the previous 12 months of TOBS data for that station.
* Plot the results as a histogram with bins=12:

_12 Months of Temperature Observation Chart_

![12-mos-TOBS](https://github.com/SteveTuttle/sqlalchemy-challenge/blob/main/Images/12_mo_TOBS.png)

### Part-2: Design Your Climate App
For this part, we will design a Flask API called __app_SDT.py__ based on the queries created with Jupyter notebook.

Per the challenge instructions, we are creating the following routes as well as specific parameters:
1) Home Route
__/__
* Start at the homepage.
* List all the available routes.

2) Precipitation Route
__/api/v1.0/precipitation__
* Convert the query results from your __precipitation analysis__ _(only the last 12 months of data)_ __to a dictionary using date as the key and prcp as the value.__
* Return the JSON representation of your dictionary.

3) Stations Route
__/api/v1.0/stations__
* Return a JSON __list of stations from the dataset.__

4) Temperature Observation Route
__/api/v1.0/tobs__
* Query the __dates and temperature observations of the most-active station for the previous year of data.__
* Return a JSON list of temperature observations for the previous year.

5) Start date _OR_ Start & End date Route
__/api/v1.0/<start> and /api/v1.0/<start>/<end>__
* Return a JSON list of the __minimum, average, and maximum temperature__ for a specified start or start-end range.
* For a specified start, calculate _TMIN_, _TAVG_, and _TMAX_ for all the dates greater than or equal to the start date.
* For a specified start date and end date, calculate _TMIN_, _TAVG_, and _TMAX_ for the dates from the start date to the end date, inclusive.

## Resources
### Bootcamp References
Module 10 Instructions

starter_code:
* app.py
* climate_starter.ipynb

Resources folder:
* hawaii_measurements.csv
* hawaii_stations.csv
* hawaii.sqlite

***Special Thanks:***
* Jamie Miller
* Mounika Mamindla
* Lisa Shemanciik

### External References
_(where possible will provide link to website)_
* [pandas documentation](https://pandas.pydata.org/docs/reference/general_functions.html)
* [matplotlib documentation](https://matplotlib.org/stable/index.html)
* [SQLAlchemy documentation](https://docs.sqlalchemy.org/en/20/)
* [Flask documentation](https://flask.palletsprojects.com/en/2.3.x/)
* YouTube _(various tutorials)_
