import snap
import os

FIn = snap.TFIn(os.path.join(os.getcwd(), 'data', "2015-01-01.graph"))
Graph = snap.TNEANet.Load(FIn)
snap.SaveEdgeList(Graph, "test.txt", "Save as tab-separated list of edges")
