import networkx as nx
import os
import sys

mapped_data_path = os.getcwd() + "/mapped_data"
shift_path = os.getcwd() + "/shift"
N = int(sys.argv[1])

graphs = []

#create the respective graphs
for file in os.scandir(mapped_data_path):
    if(file.name[-2:] != "md"):
        graphs.append((nx.read_edgelist(file.path),file.name))

#print output file for each graph into "CI_Heap_input" folder
dir_path = os.getcwd() + "/CI_Heap_input"


#iterate over all the created graphs
for graph in graphs:

    #create dictionary of all nodes and their neighbors
    output = {}
    for node in graph[0].nodes:
            output[int(node)] = list(graph[0].neighbors(node))
    

    """
    #if the node was not in the list then add an empty list
    for i in range(1, N+1):
        try:
            output[i]
        except KeyError:
            output[i] = []
    """
    
    
    #sort output dictionary according to integer key
    sorted_output = dict(sorted(output.items()))

    #get integer value of first node
    shift = next(iter(sorted_output)) - 1
    with open(shift_path + "/" + graph[1][:-23] + ".txt", "w") as f:
        f.write(str(shift))

    #print results into output file
    with open(dir_path + "/" + graph[1][:-23] + ".txt", "w") as f:

        for key, values in sorted_output.items():

            #write node
            f.write("{0} ".format(key - shift))

            #write neighbors
            for element in values:
                f.write("{0} ".format(str(int(element) - shift)))
            f.write("\n")
    """
    with open(dir_path + "/" + graph[1][:-23] + ".txt", "w") as f:

        for node in graph[0].nodes:

            #write first node
            f.write("{0} ".format(node))

            #write neighbors
            for element in graph[0].neighbors(node):
                f.write("{0} ".format(element))

            f.write("\n")
    """