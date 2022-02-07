#!/usr/bin/env python3

import csv
import numpy as np
import as_utils
import matplotlib.pyplot as plt

from lab import visibility
from algorithm import implementation
import sys

if __name__ == "__main__":

    # Retrieve information from the command line ################################################## 
    if len(sys.argv) !=2:
        print("You should provide the path to the csv environment: ")
        print("Provide the correct number of arguments (1) in the following format as str: ")
        print("Path to env_X.csv, where X is the environment number")
        exit()
    else:
        path = sys.argv[1]

    print("Specified environment", path,"\n")
    #################################################################################################

    # Defining the environment to be used
    graph = visibility(path)

    # Extracting obstacles' edges and the corresponding vertexes
    E, vertexes = graph.get_edges_vertexes()

    # Plot the obstacles in the environment
    graph.plot_edges(E)

    # Implement the Rotational Plane Sweep Algorithm for creating visibility edges 
    rspa = implementation(vertexes,E)
    v_edges = rspa.rotational_sweep()

    # Plotting Visibility Edges
    graph.plot_visibility(v_edges)

    # Plotting each vertex in the environment
    graph.plot_vertexes(vertexes)

    # Printing each visibility edge detected
    visibility_edges_list = graph.print_visibility_edges( v_edges, vertexes)


    with open("visibility_graph_"+path.split("/")[1], 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["# Format: initial edge vertex, final edge vertex"])
        for i in visibility_edges_list:
            writer.writerow([str(i[0]),str(i[1])])


    plt.show()
