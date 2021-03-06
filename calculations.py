# this script takes in the binary files for each day and performs calculations on them

import os
import snap
import sys
from numpy import trapz
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load all the graphs and put them in the graphDict
# where the key is the date and the value is the SNAP graph object

# want a function that gets the nodes with the highest betweenness centrality
# and deletes them from the graph
# and then computes the size of the largest weakly connected components
def computeResiliencyBetwn(graph, toPlot):
    # degreeCentralityDict = {}
    #for N in graph.Nodes():
    Nodes = snap.TIntFltH()
    Edges = snap.TIntPrFltH()
    snap.GetBetweennessCentr(graph, Nodes, Edges, 1.0)

    ID = []
    betweenness = []
    for node in Nodes:
        ID.append(node)
        betweenness.append(Nodes[node])

    btwnCent = pd.DataFrame({'Betweenness' : betweenness}, index = ID)
    btwnCent = btwnCent.sort(['Betweenness'], ascending = False)


    fractionInLWCC = []
    fractionNodesRemoved = []
    initial_num_nodes = graph.GetNodes()
    count = 0
    for index, row in btwnCent.iterrows():
        fractionInLWCC.append(snap.GetMxWccSz(graph)*graph.GetNodes()/\
                                initial_num_nodes)
        fractionNodesRemoved.append(float(count)/initial_num_nodes)
        count += 1
        largestNode = index
        #largestNode = np.max(degreeCentralityDict, key=degreeCentralityDict.get)
        graph.DelNode(largestNode)

    y = np.array(fractionInLWCC)


    # Compute the area using the composite trapezoidal rule.
    resiliencyIndex = trapz(y, dx=float(1)/initial_num_nodes) # area under curve

    if toPlot:
        plt.plot(fractionNodesRemoved, fractionInLWCC)
        plt.xlabel('Fraction Nodes Removed')
        plt.ylabel('Fraction of Nodes still in LWCC')
        plt.title('Nodes in LWCC vs. Removal of Nodes')
        plt.show()

    return resiliencyIndex

# want a function that gets the nodes with the highest degree centrality
# and deletes them from the graph
# and then computes the size of the largest weakly connected components
def computeResiliencyDeg(graph, toPlot):
    # degreeCentralityDict = {}
    #for N in graph.Nodes():
    degreeCentralityDict = {}
    for N in graph.Nodes():
        degreeCentralityDict[N.GetId()] = N.GetOutDeg() + N.GetInDeg()

    fractionInLWCC = []
    fractionNodesRemoved = []
    initial_num_nodes = graph.GetNodes()
    for i in range(graph.GetNodes()):
        fractionInLWCC.append(snap.GetMxWccSz(graph)*graph.GetNodes()/\
                                initial_num_nodes)
        fractionNodesRemoved.append(float(i)/initial_num_nodes)
        largestNode = max(degreeCentralityDict, key=degreeCentralityDict.get)
        del degreeCentralityDict[largestNode]
        graph.DelNode(largestNode)

    y = np.array(fractionInLWCC)


    # Compute the area using the composite trapezoidal rule.
    resiliencyIndex = trapz(y, dx=float(1)/initial_num_nodes) # area under curve

    if toPlot:
        plt.plot(fractionNodesRemoved, fractionInLWCC)
        plt.xlabel('Fraction Nodes Removed')
        plt.ylabel('Fraction of Nodes still in LWCC')
        plt.title('Nodes in LWCC vs. Removal of Nodes')
        plt.show()

    return resiliencyIndex

# want a function that gets the nodes with the highest closeness centrality
# and deletes them from the graph
# and then computes the size of the largest weakly connected components
def computeResiliencyClose(graph, toPlot):
    # degreeCentralityDict = {}
    ID = []
    closeness = []
    for N in graph.Nodes():
        ID.append(N.GetId())
        closeness.append(snap.GetClosenessCentr(graph, N.GetId()))

    closeCent = pd.DataFrame({'Closeness' : closeness}, index = ID)
    closeCent = closeCent.sort(['Closeness'], ascending = False)


    fractionInLWCC = []
    fractionNodesRemoved = []
    initial_num_nodes = graph.GetNodes()
    count = 0
    for index, row in closeCent.iterrows():
        fractionInLWCC.append(snap.GetMxWccSz(graph)*graph.GetNodes()/\
                                initial_num_nodes)
        fractionNodesRemoved.append(float(count)/initial_num_nodes)
        count += 1
        largestNode = index
        #largestNode = np.max(degreeCentralityDict, key=degreeCentralityDict.get)
        graph.DelNode(largestNode)

    y = np.array(fractionInLWCC)


    # Compute the area using the composite trapezoidal rule.
    resiliencyIndex = trapz(y, dx=float(1)/initial_num_nodes) # area under curve

    if toPlot:
        plt.plot(fractionNodesRemoved, fractionInLWCC)
        plt.xlabel('Fraction Nodes Removed')
        plt.ylabel('Fraction of Nodes still in LWCC')
        plt.title('Nodes in LWCC vs. Removal of Nodes')
        plt.show()

    return resiliencyIndex

def computeShortPathDegree(graph, toPlot):
    # degreeCentralityDict = {}
    #for N in graph.Nodes():
    degreeCentralityDict = {}
    for N in graph.Nodes():
        degreeCentralityDict[N.GetId()] = N.GetOutDeg() + N.GetInDeg()

    avgEcc_deg = []
    fractionNodesRemoved = []
    initial_num_nodes = graph.GetNodes()
    for i in range(graph.GetNodes()):
        eccentricities = []
        for node in graph.Nodes():
            eccentricities.append(snap.GetNodeEcc(graph, node.GetId(), True))
        avgEcc = float(sum(eccentricities))/len(eccentricities)
        avgEcc_deg.append(avgEcc)

        fractionNodesRemoved.append(float(i)/initial_num_nodes)
        largestNode = max(degreeCentralityDict, key=degreeCentralityDict.get)
        del degreeCentralityDict[largestNode]
        graph.DelNode(largestNode)

    y = np.array(avgEcc_deg)
    maxECC = np.max(y)
    y = y/maxECC

    # Compute the area using the composite trapezoidal rule.
    eccentricityIndex = trapz(y, dx=float(1)/initial_num_nodes) # area under curve


    if toPlot:
        plt.plot(fractionNodesRemoved, avgEcc_deg)
        plt.xlabel('Fraction Nodes Removed')
        plt.ylabel('Fraction of Nodes still in LWCC')
        plt.title('Nodes in LWCC vs. Removal of Nodes')
        plt.show()

    return eccentricityIndex

def computeShortPathCloseness(graph, toPlot):
    ID = []
    closeness = []
    for N in graph.Nodes():
        ID.append(N.GetId())
        closeness.append(snap.GetClosenessCentr(graph, N.GetId()))

    closeCent = pd.DataFrame({'Closeness' : closeness}, index = ID)
    closeCent = closeCent.sort(['Closeness'], ascending = False)


    avgEcc_close = []
    fractionNodesRemoved = []
    initial_num_nodes = graph.GetNodes()
    count = 0
    for index, row in closeCent.iterrows():
        eccentricities = []
        for node in graph.Nodes():
            eccentricities.append(snap.GetNodeEcc(graph, node.GetId(), True))
        avgEcc = float(sum(eccentricities))/len(eccentricities)
        avgEcc_close.append(avgEcc)
        fractionNodesRemoved.append(float(count)/initial_num_nodes)
        count += 1

        largestNode = index
        graph.DelNode(largestNode)

    y = np.array(avgEcc_close)
    maxECC = np.max(y)
    y = y/maxECC

    # Compute the area using the composite trapezoidal rule.
    eccentricityIndex = trapz(y, dx=float(1)/initial_num_nodes) # area under curve

    if toPlot:
        plt.plot(fractionNodesRemoved, y)
        plt.xlabel('Fraction Nodes Removed')
        plt.ylabel('Average Eccentricity')
        plt.title('Average Eccentricity')
        plt.show()

    return eccentricityIndex





# ----------------------------------------------------------------------

directory = os.path.join(os.getcwd(), 'data')

# Calculate Betweenness Centrality Resiliency Plot
'''
btwn_resiliency = []
counter = 0
for date in os.listdir(directory):
    FIn = snap.TFIn(os.path.join(os.getcwd(), 'data', date))
    G4 = snap.TNEANet.Load(FIn)
    btwn_resiliency.append(computeResiliencyBetwn(G4, False))

print btwn_resiliency
f = open("temp_btwn_res.txt", 'w')
for itm in btwn_resiliency:
    f.write("%f\n" % itm)
'''

# Calculate Closeness Centrality Longest Shortest Path Plot
short_path_close = []
counter = 0
for date in os.listdir(directory):
    FIn = snap.TFIn(os.path.join(os.getcwd(), 'data', date))
    G4 = snap.TNEANet.Load(FIn)
    short_path_close.append(computeShortPathDegree(G4, False))

print short_path_close
f = open("short_path_degree.txt", 'w')
for itm in short_path_close:
    f.write("%f\n" % itm)
