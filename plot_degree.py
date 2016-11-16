import snap
import os
import matplotlib.pyplot as plt

FIn = snap.TFIn(os.path.join(os.getcwd(), 'data', "2015-01-01.graph"))
graph = snap.TNEANet.Load(FIn)

# plot degree distribution
# get number of nodes of each degree
graph_dd = snap.TIntPrV()
snap.GetDegCnt(graph, graph_dd)

# create two vectors to store the count and the degree
count = []
degree = []

for item in graph_dd:
    count.append(item.GetVal2())
    degree.append(item.GetVal1())

# plot
g1, = plt.plot(degree, count,marker="+",markersize=5)
plt.title("Degree Distribution for 01-01-2015 graph")
plt.ylabel("Fraction of Nodes")
plt.xlabel("Degree of Node")
plt.show()
