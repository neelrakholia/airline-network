import sys
import matplotlib.pyplot as plt
import csv

with open(sys.argv[1], 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)[0]

#
# plt.plot(range(1, len(data)+1), data, marker='o', markersize = '3')
# plt.xlabel('Day of Year')
# plt.ylabel('Resiliency Index')
# plt.title('Resiliency Index by Day of Year (Betweenness Centrality)')
# plt.show()


plt.plot(range(1, len(data)+1), data, marker='o', markersize = '3')
plt.xlabel('Day of Year')
plt.ylabel('Resiliency Index')
plt.title('Resiliency Index by Day of Year (Closeness Centrality)')
plt.show()
