# run this by doing in terminal:
# python plot_resiliency.py short_path_close.txt

import sys
import matplotlib.pyplot as plt
import csv

with open(sys.argv[1], 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)[0]

for x in range(len(data)):
    data[x] = float(data[x])

#
# plt.plot(range(1, len(data)+1), data, marker='o', markersize = '3')
# plt.xlabel('Day of Year')
# plt.ylabel('Resiliency Index')
# plt.title('Resiliency Index by Day of Year (Betweenness Centrality)')
# plt.show()

'''
plt.plot(range(1, len(data)+1), data, marker='o', markersize = '3')
plt.xlabel('Day of Year')
plt.ylabel('Resiliency Index')
plt.title('Resiliency Index by Day of Year (Closeness Centrality)')
plt.show()
'''


plt.plot(range(1, len(data)+1), data, marker='.')
plt.xlabel('Day of Year')
plt.ylabel('Eccentricity Index')
plt.title('Eccentricity Index by Day of Year (Closeness Centrality)')
plt.show()
