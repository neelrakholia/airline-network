import os
import snap
import sys
import pandas as pd
import numpy as np

directory = os.path.join(os.getcwd(), 'data')

mean_nodes = []
mean_edges = []
average_out_degree = []
average_in_degree = []
average_max_in_degree = []
average_max_out_degree = []
counter = 0
for date in os.listdir(directory):
    FIn = snap.TFIn(os.path.join(os.getcwd(), 'data', date))
    G = snap.TNEANet.Load(FIn)
    mean_nodes.append(G.GetNodes())
    mean_edges.append(G.GetEdges())
    DegToCntV = snap.TIntPrV()
    snap.GetInDegCnt(G, DegToCntV)
    sum_in = 0
    for item in DegToCntV:
        sum_in += item.GetVal2()*item.GetVal1()

    average_in_degree.append(sum_in/float(G.GetNodes()))

    DegToCntV = snap.TIntPrV()
    snap.GetOutDegCnt(G, DegToCntV)
    sum_out = 0
    for item in DegToCntV:
        sum_out += item.GetVal2()*item.GetVal1()

    average_out_degree.append(sum_out/float(G.GetNodes()))

    max_in_node = snap.GetMxInDegNId(G)
    max_out_node = snap.GetMxOutDegNId(G)

    average_max_in_degree.append(G.GetNI(max_in_node).GetInDeg())
    average_max_out_degree.append(G.GetNI(max_out_node).GetOutDeg())

print "Mean number of nodes ", np.mean(mean_nodes)
print "Mean number of edges ", np.mean(mean_edges)
print "Mean number of out edges ", np.mean(average_out_degree)
print "Mean number of in edges ", np.mean(average_in_degree)
print "Mean of max number of out edges ", np.mean(average_max_out_degree)
print "Mean of max number of in edges ", np.mean(average_max_in_degree)
