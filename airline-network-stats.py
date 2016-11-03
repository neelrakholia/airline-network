###############################################################################
# Input nodes: airports.csv--list of all airports used
# Input edges: 15-01-network-data.csv--list of all flights operating in Janurary 2015

###############################################################################

# import modules
import snap
import numpy as np
import matplotlib.pyplot as plt
import sys

# columns to search for node ids
COL_ORIGIN = 3
COL_DEST = 5

###############################################################################

# create a function to read a file and load nodes
def loadnodes(filename):

    # create an empty graph
    air_graph = snap.TNEANet.New()

    # open file
    with open(filename) as f:
        next(f)

        for line in f:
            row = line.strip().split(',')
            row[0] = row[0].replace('"', '')

            # add nodes and check for uniqueness
            try:
                air_graph.AddNode(int(row[0]))
            except:
                pass

    # return graph
    return air_graph

# create a function to read a file and load edges
def loadedges(filename, air_graph):

    # open file
    with open(filename) as f:
        next(f)

        eid = 0
        date = "2015-01-01"

        for line in f:

            # get attributes
            row = line.strip().split(',')

            # make a new graph for a new date
            if date != row[0]:
                air_graph = snap.GetMxWcc(air_graph)
                tosave = snap.TFOut(date + ".csv")
                air_graph.Save(tosave)
                print air_graph.GetNodes()
                tosave.Flush()

                # make a fresh copt of the graph
                air_graph = loadnodes(sys.argv[1])


            # add edge and attributes
            air_graph.AddEdge(int(row[COL_ORIGIN]), int(row[COL_DEST]), \
            eid)
            air_graph.AddIntAttrDatE(eid, int(row[1]), "Airline-ID")
            air_graph.AddIntAttrDatE(eid, int(row[2].replace('"', '')), \
            "Flight-No")

            # update edge index
            eid += 1

            # update date
            date = row[0]

        # save the last graph
        air_graph = snap.GetMxWcc(air_graph)
        tosave = snap.TFOut(date + ".csv")
        air_graph.Save(tosave)
        print air_graph.GetNodes()
        tosave.Flush()
        air_graph = loadnodes(sys.argv[1])

###############################################################################

# read nodes
print sys.argv[1]
air_graph = loadnodes(sys.argv[1])
loadedges(sys.argv[2], air_graph)

print air_graph.GetNodes()
print air_graph.GetEdges()

reid = air_graph.GetRndEId()
print air_graph.GetIntAttrDatE(10, "Flight-No")
print air_graph.GetIntAttrDatE(10, "Airline-ID")
