#takes in one of the layers and creates an integer node mapping and outputs it into a file in the following format
#   node_name   integer_value


import csv
import os
import networkx as nx
import matplotlib.pyplot as plt
import sys

#create unified graph that has all necessary nodes
dir_path = os.getcwd() + "/raw_data"

graphs = []

for file in os.scandir(dir_path):
    if(file.name[-2:] != "md"):
        graphs.append(nx.read_weighted_edgelist(file.path))

G = graphs[0]

for H in graphs:
    G = nx.compose(G, H)

#get node list
node_list = list(G.nodes)

#write mapping 
with open("mapping.txt", 'w') as f:
    for i in range(len(node_list)):
        f.write("{0} {1}".format(node_list[i], i))
        f.write('\n')

print(len(node_list))