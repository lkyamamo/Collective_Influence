import os

collective_influence = os.getcwd()

influencer_ranking_path = collective_influence + "/Influencer_ranking"
results_path = collective_influence + "/results/"


for file in os.scandir(influencer_ranking_path):
    if(file.name[-2:] != "md"):

        #map back to original integer value

        file_path = collective_influence + "/secondary_mapping/" + (file.name.split()[0])[12:-10] + ".txt"

        print(file_path)