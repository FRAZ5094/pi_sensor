import datetime
import sys
from itertools import islice

import matplotlib.pyplot as plt

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
plt.figure(1)
plt.plot(times, temps)
plt.title("Temperature over time")
# plt.ylim(0, 50)
plt.grid()
plt.figure(2)
plt.plot(times, humids)
plt.title("Humidity over time")
plt.grid()
plt.show()
