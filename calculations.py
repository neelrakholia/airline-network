# this script takes in the binary files for each day and performs calculations on them

directory = os.path.join(os.getcwd(), 'data')
graphDict = {}

# load all the graphs and put them in the graphDict
# where the key is the date and the value is the SNAP graph object
for date in os.listdir(directory):
    FIn = TFIn(date)
    G4 = TNGraph.Load(FIn)
    graphDict[date] = G4

# want a function that gets the nodes with the highest betweenness centrality
# and deletes them from the graph
# and then computes the size of the largest weakly connected components
def computeResiliency(graph):
    degreeCentralityDict = {}
    for N in graph.Nodes():
        degreeCentralityDict[N.GetId()] = snap.GetDegreeCentr(graph, NI.GetId())

    fractionInLWCC = []
    fractionNodesRemoved = []
    for i in range(graph.GetNodes()):
        fractionInLWCC.append(snap.GetMxWccSz(graph))
        fractionNodesRemoved.append(float(i)/graph.GetNodes())
        largestNode = max(degreeCentralityDict, key=degreeCentralityDict.get)
        graph.DelNode(largestNode)

    plt.plot(fractionNodesRemoved, fractionInLWCC)
    plt.xlabel('Fraction Nodes Removed')
    plt.ylabel('Fraciton of Nodes still in LWCC')
    plt.title('Nodes in LWCC vs. Removal of Nodes')
    plt.show()



#for date, graphObject in graphDict.iteritems():
#    computeResiliency(graphObject)
