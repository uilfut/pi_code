import plotly.plotly as py
import json
import time
import datetime as dt
import plotly.graph_objs as go
import numpy as np
import sqlite3
import pandas as pd
# from sqlalchemy import create_engine


# py.sign_in("uilfut", "9qyY9cwWd0H3RT1fergd")

con = sqlite3.connect('/home/pi/environment.db')
#c = conn.cursor()
df = pd.read_sql_query("SELECT date_time, temp2 FROM readings", con)

df['temp2_MA'] = df.temp2.rolling(10).mean()

trace1 = go.Scatter(
        x=df.date_time,
        y=df.temp2_MA
        )
py.plot([trace1])

con.close()
#    temp_reading = sensor.get_temperature(W1ThermSensor.DEGREES_C)
#    time.sleep(60)



