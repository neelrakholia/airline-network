import snap
import os

FIn = snap.TFIn(os.path.join(os.getcwd(), 'data', "2015-01-01.graph"))
Graph = snap.TNEANet.Load(FIn)
labels = snap.TIntStrH()
for NI in Graph.Nodes():
    labels[NI.GetId()] = str(NI.GetId())
snap.DrawGViz(Graph, snap.gvlDot, "output.png", " ", labels)
