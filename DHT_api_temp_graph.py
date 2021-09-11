import datetime
import sys
from itertools import islice

import matplotlib.pyplot as plt
import pandas as pd

filename = "living_room_and_api_temp_log"
times = []
DHT_temps = []
api_temps = []
with open(filename, "r") as f:
    for line in islice(f, 1, None):
        cols = line.split(",")
        if len(cols) > 1:
            time, DHT_temp, api_temp = cols
            times.append(datetime.datetime.fromtimestamp(int(time)))
            DHT_temps.append(float(DHT_temp))
            api_temps.append(float(api_temp))

data = pd.DataFrame({"time": times, "DHT_temp": DHT_temps, "api_temp": api_temps})
print(data.tail())

plt.figure(0)
plt.plot(data["time"], data["DHT_temp"], label="Inside temperature")
plt.plot(data["time"], data["api_temp"], label="Outside temperature")
plt.legend()
plt.ylabel(f"Temperature {chr(176)}C")
plt.title("Inside and Outside temperature over time")
plt.show()
