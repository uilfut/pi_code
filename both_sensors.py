import sqlite3
import time
import Adafruit_DHT

while True:
    humid, temp = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
    conn = sqlite3.connect('/home/pi/environment.db')
    c = conn.cursor()
    c.execute("INSERT INTO 'readings' (date_time, temp, humid) VALUES (DATETIME('now','localtime'),?,?)", (temp, humid))
    conn.commit()
    conn.close()
    time.sleep(60)

#print(tempC)

# DATETIME('now');
