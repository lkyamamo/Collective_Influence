import os
import networkx as nx

dir_path = os.getcwd() + "/mapped_data"

graphs = []

#create the respective graphs
for file in os.scandir(dir_path):
    if(file.name[-2:] != "md"):
        graphs.append((nx.read_edgelist(file.path),file.name))

for graph in graphs:
    print(graph[1][:-23])