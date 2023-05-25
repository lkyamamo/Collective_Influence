import networkx as nx
import os

dir_path = os.getcwd() + "/mapped_data"

graphs = []

#create the respective graphs
for file in os.scandir(dir_path):
    if(file.name[-2:] != "md"):
        graphs.append((nx.read_edgelist(file.path),file.name))

#print output file for each graph into "CI_Heap_input" folder
dir_path = os.getcwd() + "/CI_Heap_input"

for graph in graphs:

    with open(dir_path + "/" + graph[1][:-23] + ".txt", "w") as f:

        for node in graph[0].nodes:

            #write first node
            f.write("{0} ".format(node))

            #write neighbors
            for element in graph[0].neighbors(node):
                f.write("{0} ".format(element))

            f.write("\n")
