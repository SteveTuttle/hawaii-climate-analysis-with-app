# Import the dependencies.
from flask import Flask, jsonify

# Python SQL toolkit and Object Relational Mapper from climate_analysis
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import numpy as np
import pandas as pd
import datetime as dt

#################################################
# Database Setup
#################################################
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
# Home
@app.route("/")
def home():
    """Home route listing all site path options"""
    return (
        f"Hawaii Precipitation and Temperature: 08/2016 - 08/2017<br/>"
        f"Available Routes: <br>"
        f"/api/v1.0/precipitation <br>"
        f"/api/v1.0/stations <br>"
        f"/api/v1.0/tobs <br>"
        f"/api/v1.0/start <br>"
        f"/api/v1.0/start/end <br>"
        f"note: start and end dates must be in YYYYMMDD format<br>"
    )

# Precipitation
@app.route("/api/v1.0/precipitation")
def prcp_link():
    """Precipitation data in HI as JSON from 08/2016 - 08/2017"""
    # Calculate the date one year from the last date in data set.
    one_year_ago = dt.datetime.strptime('2017-08-23', '%Y-%m-%d') - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    HI_prcp_query = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()

    # Close Session
    session.close()

    # creating dictionary using date as the key prcp as the value
    date_prcp = {date: prcp for date, prcp in HI_prcp_query}

    # Return jsonify version of data
    return jsonify(date_prcp)

# Stations
@app.route("/api/v1.0/stations")
def station_link():
    """Station list in HI as JSON from 08/2016 - 08/2017"""
    station_names = session.query(Station.station).all()

    # Close Session
    session.close()

    # unravel station_names list
    list_stations = list(np.ravel(station_names))

    # Return jsonify version of data
    return jsonify(Stations = list_stations)

# Temperature
@app.route("/api/v1.0/tobs")
def temp_link():
    """Temperature data for most active station as JSON from 08/2016 - 08/2017"""
    # Calculate the date one year from the last date in data set.
    one_year_ago = dt.datetime.strptime('2017-08-23', '%Y-%m-%d') - dt.timedelta(days=365)

    # Query the last 12 months of temperature observation data for this station
    twelve_mo_temp_query = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= one_year_ago).all()
    
    # Close Session
    session.close()

    # unravel temp query list
    list_temps = list(np.ravel(twelve_mo_temp_query))

    # Return jsonify version of data
    return jsonify(Temperatures = list_temps)

# Start date or Start and End date temperature for station USC00519281
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def start_temp(start=None, end=None):
    """Return TMIN, TAVG, & TMAX for most active station as JSON from 08/2016 - 08/2017"""

    # using select to perform temperature calcalations
    sel = [func.min(Measurement.tobs),
        func.avg(Measurement.tobs),
        func.max(Measurement.tobs)]

    # Calculating TMIN, TAVG, & TMAX greater than start date
    if not end:

        start = dt.datetime.strptime(start, '%Y%m%d')

        temp_calc = session.query(*sel).\
            filter(Measurement.station == 'USC00519281').\
            filter(Measurement.date >= start).all()
        
        # Close Session
        session.close()
        
        # unravel temp_cal list for start date
        list_temp_stats = list(np.ravel(temp_calc))

        # Return jsonify version of data
        return jsonify(min_avg_max_Temps = list_temp_stats)

    # Calculating TMIN, TAVG, & TMAX between start and end date
    start = dt.datetime.strptime(start, '%Y%m%d')
    end = dt.datetime.strptime(end, '%Y%m%d')

    temp_calc = session.query(*sel).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    
    # Close Session
    session.close()
    
    # unravel temp_cal list for start and end date
    list_temp_stats = list(np.ravel(temp_calc))

    # Return jsonify version of data
    return jsonify(min_avg_max_Temps = list_temp_stats)

if __name__ == "__main__":
    app.run(debug=True)

