import time

from DH11_22_temp_humid import get_DHT_temp_humid
from weather_api import get_temp_api

id = "2648579"
units = "metric"
api_data = get_temp_api(id, units)
DHT_data = get_DHT_temp_humid(max_attempts=30)
print(f"{int(time.time())},{DHT_data['temperature']},{api_temp}")
