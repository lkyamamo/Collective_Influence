import networkx as nx
import os
import sys

mapped_data_path = os.getcwd() + "/mapped_data"

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
    
    
    #sort output dictionary according to integer key
    sorted_output = dict(sorted(output.items()))

    #print results into output file
    with open(dir_path + "/" + graph[1][:-23] + ".txt", "w") as f:

        for key, values in sorted_output.items():

            #write node
            f.write("{0} ".format(key))

            #write neighbors
            for element in values:
                f.write("{0} ".format(element))
            f.write("\n")
"""
old implementation

    #map nodes to be sequential keys will be the original non-sequential integers and the values with be the new sequential values
    integer_mapping = {}
    i = 1
    for key in sorted_output:
        integer_mapping[key] = i
        i += 1

    with open(secondary_mapping_path + "/" + graph[1][:-23] + ".txt", 'w') as f:
        for key,value in integer_mapping.items():
            f.write("{0} {1}\n".format(key,value))

    output = {}

    #convert the sorted_output
    for key,values in sorted_output.items():
        output[integer_mapping[key]] = []
        for element in values:
            output[integer_mapping[key]].append(integer_mapping[int(element)])

    #print results into output file
    with open(dir_path + "/" + graph[1][:-23] + ".txt", "w") as f:

        for key, values in output.items():

            #write node
            f.write("{0} ".format(key))

            #write neighbors
            for element in values:
                f.write("{0} ".format(element))
            f.write("\n")
    """
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

