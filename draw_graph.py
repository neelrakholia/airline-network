import snap
import os

FIn = snap.TFIn(os.path.join(os.getcwd(), 'data', "2015-01-01.graph"))
Graph = snap.TNEANet.Load(FIn)
# # labels = snap.TIntStrH()
# # for NI in Graph.Nodes():
# #     labels[NI.GetId()] = str(NI.GetId())
# snap.DrawGViz(Graph, snap.gvlDot, "graph.png", "graph 1")
#snap.DrawGViz(Graph, snap.gvlDot, "output.png", " ", labels)
# NIdColorH = snap.TIntStrH()
# NIdColorH[0] = "green"
# NIdColorH[1] = "red"
# NIdColorH[2] = "purple"
# NIdColorH[3] = "blue"
# NIdColorH[4] = "yellow"
#Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
snap.DrawGViz(Graph, snap.gvlSfdp, "network.png", "graph 3", True)
