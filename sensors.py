import sqlite3
import time
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

while True:
    conn = sqlite3.connect('/home/pi/environment.db')
    c = conn.cursor()
    tempC = float(sensor.get_temperature(W1ThermSensor.DEGREES_C))
    c.execute("INSERT INTO 'readings' (date_time, temp2, humid) VALUES (DATETIME('now','localtime'),?, '123')", (tempC,))
    conn.commit()
    conn.close()
    time.sleep(60)

