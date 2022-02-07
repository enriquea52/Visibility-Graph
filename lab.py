import csv
import numpy as np
import as_utils
import matplotlib.pyplot as plt

# The present visibility class is mainly used for specific utilities such as plotting and printing results
# in order to have better code organization 
class visibility(object):
    def __init__(self , map):
        self.map = map


    def get_edges_vertexes(self):
        # This function reads a csv file to retrieve the vertexes in the enviornment (start, goal and obstacles' vertexes)
        # It creates a dictionary of list where each list represents the vertexes in a specific obstacle
        v = []
        with open(self.map,'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                v.append(row)

        v = np.array(v)
        v = v.astype(float)

        vertexes_dict = {}


        for i in v:
            if not(bool(vertexes_dict.get(int(i[0])))):
                vertexes_dict[int(i[0])] = []
            vertexes_dict[int(i[0])].append(as_utils.Point(i[1],i[2]))
        
        # This function also computes the Edges of each obstacle consdiering the vertexes that define it 
        E = []
        #Create obstacle edges
        for i in range(1,len(vertexes_dict)-1):
            for j in range(0,len(vertexes_dict[i])-1):
                E.append(as_utils.Segment(vertexes_dict[i][j],vertexes_dict[i][j+1]))
            E.append(as_utils.Segment(vertexes_dict[i][len(vertexes_dict[i])-1],vertexes_dict[i][0]))

        return E, vertexes_dict

    def plot_edges(self, edges):
        # The purpose of the function is to plot the obstacles' edges
        for j in edges:
            plt.plot([j.p1.x,j.p2.x], [j.p1.y,j.p2.y],color = 'black',linewidth=3) 

    def plot_vertexes(self, vertexes):
        # The purpose of the function is to plot vertexes in the environment
        counter = 0
        for i in range(0,len(vertexes)):
            for j in vertexes[i]:
                plt.scatter(j.x, j.y,color = 'green',zorder=3) 
                plt.annotate(counter, (j.x+0.1, j.y))
                counter +=1


    def plot_visibility(self, visibility_edges):
        # The purpose of the function is to plot the visibility edges emanating from each vertex
        for j in visibility_edges:
            plt.plot([j.p1.x,j.p2.x], [j.p1.y,j.p2.y],color = 'blue',linestyle = 'dashed')   

    def print_visibility_edges(self, visibility_edges, vertexes):
        # This function prints a list of edges.
        # Each edge is composed of an initial vertex and a final vertex.
        # both vertexes are represented with respect their order of appearance in the csv file.
        a = None # First vertex
        b = None # Second vertex
        v_list = []
        for edge in visibility_edges:
            counter = 0
            for i in range(0,len(vertexes)):
                for j in vertexes[i]:
                    if j.x == edge.p1.x and j.y == edge.p1.y:
                        a = counter
                    counter += 1
            counter = 0
            for i in range(0,len(vertexes)):
                for j in vertexes[i]:
                    if j.x == edge.p2.x and j.y == edge.p2.y:
                        b = counter
                    counter += 1
            v_list.append((a,b))
        print("Printing ",len(v_list)," visibility edges...")
        print(v_list)
        return v_list
            





