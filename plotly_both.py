import plotly.plotly as py
import json
import time
import datetime as dt
import plotly.graph_objs as go
import numpy as np
import sqlite3
import pandas as pd

con = sqlite3.connect('/home/pi/environment.db')
#c = conn.cursor()
df = pd.read_sql_query("SELECT date_time, temp, humid FROM readings WHERE date_time > '2018-03-07'", con)
con.close()

df['temp_MA'] = df.temp.rolling(10).mean()
df['humid_MA'] = df.humid.rolling(10).mean()

trace1 = go.Scatter(
        name = 'Temperature degC',
        x=df.date_time,
        y=df.temp_MA,
        yaxis = 'y1',
        mode = 'lines'
        )
trace2 = go.Scatter(
        name = 'Rel Humidity %',
        x=df.date_time,
        y=df.humid_MA,
        yaxis = 'y2',
        fill = 'tozeroy'
        )
data = [trace1, trace2]
layout = go.Layout(
        yaxis1=dict(
            title='Temperature deg C',
            side='left'
            ),
        yaxis2=dict(
            title='Humidity Rel %',
            side='right',
            overlaying='y'
            )
        )
fig = go.Figure(data=data, layout=layout)
py.plot(fig)

