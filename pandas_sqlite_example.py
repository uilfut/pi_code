import pandas as pd
import sqlite3
import pandas.stats.moments

con = sqlite3.connect("/home/pi/environment.db")

df = pd.read_sql_query("SELECT date_time, temp, humid FROM readings WHERE date_time > '2018-03-07'", con)

#df.temp2 = df.temp2.astype(float)

df['MA_temp'] = df.temp.rolling(3).mean()
df['MA_humid'] = df.humid.rolling(3).mean()

print(df)

con.close()



