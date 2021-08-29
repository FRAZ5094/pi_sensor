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
            times.append(int(time))
            temps.append(int(temp))
            humids.append(int(humid))

plt.plot(times, temps)
plt.ylim(0, 50)
plt.show()
