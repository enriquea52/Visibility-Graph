import numpy as np
import as_utils
import matplotlib.pyplot as plt
import matplotlib.path as mplPath


# The present class is the implementation of the Rotational Plane Sweep Algorithm used
# for building visibility graphs.
# this class includes all the function definitions required to achieve the application.
class implementation(object):

    def __init__(self, vertexes, edges):
        self.vertexes = vertexes
        self.obstacles_edges = edges

    def get_vertexes_from_dict(self, v_dict): # This function retrieves vertexes from a dictionary of lists and converts it to a list of vertexes.
        vertexes = []
        for i in v_dict:
            for i in v_dict[i]:
                vertexes.append(i)
        return vertexes

    
    def angle(self,y,x): # Make an angle from 0 to 2pi for sorting purposes
        angle = np.arctan2(y,x)
        if angle < 0:
            angle = (angle + 2*np.pi)
        return angle

    def copy_vertex_list(self,list): # Function for copying a list of vertexes safely 
        new_list = []
        for vertex in list:
            new_list.append(as_utils.Point(vertex.x,vertex.y))
        return new_list

    def S_inicialization(self,half_line, current_vertex): 
        # This function initializes the S list by creating an horizontal halfline with 0 degrees with respect the global x axis.
        # Every edge in the environment intersecting the half line will be added to the S list.
        # The S list will be sorted depending on which edge was intersected first.
        S = []
        for edge in self.obstacles_edges:
            is_interset = half_line.intersect(edge)
            temp_point= half_line.intersection_point(edge)
            if (is_interset[0] and round(current_vertex.dist(temp_point),0) != 0):
                edge.distance = current_vertex.dist(temp_point)
                S.append(edge)
        S = sorted(S, key=lambda x: x.distance)

        return S

    def is_visible(self,v,vi,s, sweep_line):
        # This function returns True if a vertex vi is visible from a vertex v,
        # Otherwise it returns false.
        # It follows a checklist for corroborating if the vertex vi is visible from different criteria

        # If the S list is empty the vertex vi is visible from v
        if len(s) == 0: 
            return True
        # If both v and vi lay on the same edge in S, vi is visible from v
        for i in s:       
            if round(v.dist_segment(i),3) == 0. and round(vi.dist_segment(i),3) == 0.:
                return True
        # If vi and v are on the same obstacle and if the midpoint between them is inside the obstacle
        # vi is not visible from v
        if self.inside_poligon(v,vi,s):
            return False
        # If the first edge in S intersect the sweepline going from v to vi, vi is not visible from v
        for edge in s:
            is_interset = sweep_line.intersect(edge)
            if is_interset[0] and not(round(v.dist_segment(edge),3) == 0.):
                return False
            else:
                return True


    def inside_poligon(self, v, vi, s):
        # First check if both vertexes belong to the same obstacle
        id1 = None
        id2 = None
        for i in range(0,len(self.vertexes)):
            for j in self.vertexes[i]:
                if (v.x,v.y) == (j.x,j.y):
                    id1 = i
                if (vi.x,vi.y) == (j.x,j.y):
                    id2 = i
        # If both vertexes belong to the same obstacle, and the midpoint between them is inside an obstacle, vi is not visible from v
        if id1 == id2:
            poly_path = mplPath.Path(np.array([[vertex.x,vertex.y] for vertex in self.vertexes[id1]]))            
            midpoint = ((v.x+vi.x)/2, (v.y+vi.y)/2)
            return poly_path.contains_point(midpoint)
        else:
            return False

    def remove_repeated(self, visible): # Function used to remove repeated visibility edges from the final visibility edge list
        i = 0
        j = 1   
        while i<len(visible) - 1:
            while j<len(visible):
                if (visible[i].p1.x == visible[j].p2.x and visible[i].p1.y == visible[j].p2.y and visible[i].p2.x == visible[j].p1.x and visible[i].p2.y == visible[j].p1.y) :
                    visible.remove(visible[j])
                    break
                j+=1
            i+=1
            j = i+1

        return [ x for x in visible if not(x.p1.x == x.p2.x and x.p1.y == x.p2.y)]

                    



    def rotational_sweep(self): # Rotational Plane Sweep Algorithm Implementation
        
        vertexes = self.get_vertexes_from_dict(self.vertexes)
        sorted_vertexes = self.copy_vertex_list(vertexes)
        visibility = []

        for k in range(0,len(vertexes)):
            v = vertexes[k] # Vertex to check visibility from 

            # Sort vertexes according to the angle 
            for point in sorted_vertexes:
                point.alpha(self.angle(point.y-v.y,point.x-v.x))

            sorted_vertexes = sorted(sorted_vertexes, key=lambda x: x.alph)

            half_line = as_utils.Segment(v,as_utils.Point(v.x+100,v.y))

            # S list inizialization
            S = self.S_inicialization(half_line, vertexes[k])
           

            
            for vi in sorted_vertexes: # Start to check visibility of vi with respect v

                for edge in self.obstacles_edges: # S list update
                    if round(vi.dist_segment(edge),2) == 0. and edge not in S:
                        S.append(edge)
                    elif (round(vi.dist_segment(edge),2) == 0.  and edge in S) or (round(v.dist_segment(edge),2) == 0. and edge in S):
                        S.remove(edge)
                    
                
                # create a sweep line from vertex v to vi with an angle offset of 0.001 and a magnitude of 100
                vi_SL = as_utils.Point(v.x+(100)*np.cos(vi.alph + 0.001),v.y+(100)*np.sin(vi.alph + 0.001))
                sweep_line = as_utils.Segment(v,vi_SL)
                #///////////////////////////////////////////////////////////////////////////////////////////

                # Calculate the distance of the sweepline to every edge in S
                for s_edge in S:
                    temp_point= sweep_line.intersection_point(s_edge)
                    s_edge.distance = v.dist(temp_point)
                ##############################################################

                # Sort the S list with respect which obstacle edge is closer to v
                S = sorted(S, key=lambda x: x.distance)


                sweep_line1 = as_utils.Segment(v,vi)
                # Check for visibility
                if self.is_visible(v,vi,S, sweep_line1):
                    visibility.append(as_utils.Segment(v,vi))


        return self.remove_repeated(visibility) # Return the visibility edges excluding repeated ones
                


