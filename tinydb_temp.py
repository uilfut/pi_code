from tinydb import TinyDB, Query
import time
from w1thermsensor import W1ThermSensor

db = TinyDB('tinydb_environment.json')

sensor = W1ThermSensor()

while True:
    tempC = float(sensor.get_temperature(W1ThermSensor.DEGREES_C))
    db.insert({'date_time':date_time, 'tempC': tempC})
    time.sleep(60)

