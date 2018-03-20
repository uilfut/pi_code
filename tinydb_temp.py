from tinydb import TinyDB, Query
import time
from w1thermsensor import W1ThermSensor
from datetime import datetime
import json
db = TinyDB('tinydb_environment.json')

sensor = W1ThermSensor()
while True:
    tempC = float(sensor.get_temperature(W1ThermSensor.DEGREES_C))
    timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    db.insert({'date_time': timestamp, 'tempC': tempC})
    time.sleep(10)

#    time_dict = {'datetime': datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}
#    time_dict = {datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}
#    db.insert(time_dict, 'tempC': tempC})
