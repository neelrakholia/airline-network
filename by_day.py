import numpy as np
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import csv

with open(sys.argv[1], 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)[0]
# data = pd.read_csv(sys.argv[1], header = 0, names = None)
# print list(data.columns.values)


mon = []
tue = []
wed = []
thur = []
fri = []
sat = []
sun = []

count = 0
for el in data:
    elf = float(el)
    if count % 7 == 0:
        thur.append(elf)
    elif count % 7 == 1:
        fri.append(elf)
    elif count % 7 == 2:
        sat.append(elf)
    elif count % 7 == 3:
        sun.append(elf)
    elif count % 7 == 4:
        mon.append(elf)
    elif count % 7 == 5:
        tue.append(elf)
    elif count % 7 == 6:
        wed.append(elf)
    else:
        pass

    count += 1

week = [mon, tue, wed, thur, fri, sat, sun]
means = []
sd = []
for day in week:
    means.append(np.mean(day))
    sd.append(np.std(day))

fig, ax = plt.subplots()

plt.plot(range(0, 7), means)
plt.errorbar(range(0, 7), means, yerr = sd)
plt.xlim(-1, 8)
plt.title("Average Resiliency (Closeness Centrality) by Day of the Week")
plt.xlabel("Day of the Week")
plt.ylabel("Average Resiliency Index")
ax.set_xticklabels(["","Monday", "Tuesday", "Wednesday", \
"Thursday", "Friday", "Saturday", "Sunday", ""])
plt.show()
