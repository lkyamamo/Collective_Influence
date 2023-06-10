#takes in cutoff edge list from "cutoff_data" folder and creates the node mapping
#format:
#   Node_name integer


import csv
import os
import networkx as nx
import matplotlib.pyplot as plt
import sys

# Check if the command line argument is provided
if len(sys.argv) < 2:
    print("Please provide a string as a command line argument.")
    sys.exit(1)

dir_path = os.getcwd() + "/cutoff_data"

file_name = sys.argv[1]
file_name = file_name[:file_name.rfind(".")]
file_path = dir_path + "/" + sys.argv[1]

#create network the network...
G = nx.read_weighted_edgelist(file_path)

#get node listand write mapping into maps folder
node_list = list(G.nodes)
with open(os.getcwd() + "/maps/" + file_name + "_mapping.txt" , 'w') as f:
    for i in range(len(node_list)):
        f.write("{0} {1}".format(node_list[i], i+1))
        f.write('\n')



"""
multimapped implementation

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
        f.write("{0} {1}".format(node_list[i], i+1))
        f.write('\n')

print(len(node_list))
"""