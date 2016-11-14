import os
import snap
import sys
import pandas as pd
import numpy as np

directory = os.path.join(os.getcwd(), 'data')

mean_nodes = []
mean_edges = []
counter = 0
for date in os.listdir(directory):
    FIn = snap.TFIn(os.path.join(os.getcwd(), 'data', date))
    G = snap.TNEANet.Load(FIn)
    mean_nodes.append(G.GetNodes())
    mean_edges.append(G.GetEdges())

print "Mean number of nodes ", np.mean(mean_nodes)
print "Mean number of edges ", np.mean(mean_edges)
