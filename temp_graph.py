import datetime
import sys
from itertools import islice

import matplotlib.pyplot as plt
import pandas as pd

filename = sys.argv[1]

times = []
temps = []
humids = []
with open(filename, "r") as f:
    for line in islice(f, 1, None):
        cols = line.split(",")
        if len(cols) > 1:
            time, temp, humid = cols
            times.append(datetime.datetime.fromtimestamp(int(time)))
            temps.append(int(temp))
            humids.append(int(humid))
data = pd.DataFrame({"time": times, "temp": temps, "humidity": humids})
data["MA_temp_30"] = data["temp"].rolling(30, center=True).mean()
data["MA_humid_30"] = data["humidity"].rolling(30, center=True).mean()
plt.figure(1)
plt.plot(data["time"], data["temp"], label="Temperature")
plt.plot(data["time"], data["MA_temp_30"], label="Temperature (30min rolling average)")
plt.legend()
plt.title("Temperature over time")
plt.xlabel("Time")
plt.ylabel(f"Temperature ({chr(176)}C)")
plt.ylim(15, 30)
plt.grid()
plt.figure(2)
plt.plot(data["time"], data["humidity"], label="Humidity")
plt.plot(data["time"], data["MA_humid_30"], label="Humidity (30min rolling average)")
plt.legend()
plt.title("Humidity over time")
plt.xlabel("Time")
plt.ylabel("Humidity (%)")
plt.grid()
plt.show()
