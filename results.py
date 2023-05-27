import os
import re

#top = 10 #change to see however many top influencers you want
start_line = 8 #from structure of file

influencer_ranking_path = "/home/logan/Research/MediaNetworks/Collective_Influence/Influencer_ranking"
results_path = "/home/logan/Research/MediaNetworks/Collective_Influence/results/"

#create mapping from mapping.txt file
mapping = {}
with open("/home/logan/Research/MediaNetworks/Collective_Influence/mapping.txt", "r") as f:
    for line in f:
        values = line.split(' ')
        mapping[int(values[1])] = values[0]


for file in os.scandir(influencer_ranking_path):
    if(file.name[-2:] != "md"):
        with open(file.path, "r") as influencer_ranking_file:
            #create file name
            location = file.name.find('_')
            output_name = results_path + file.name[location+1:]

            with open(output_name, "w") as results_file:

                #write header
                results_file.write("Ranking\tNode\tDegree\tComponenet\n")

                #take nodes from file, convert back to names from integer, write in output file
                lines = influencer_ranking_file.readlines()[start_line - 1:]
                for line in lines:
                    numbers = re.findall(r'\d+', line)
                    numbers = [int(num) for num in numbers]
                    numbers[1] = mapping[numbers[1]]
                    results_file.write(f"{numbers[0]} \t {numbers[1]} \t {numbers[2]} \t {numbers[3]} \n")
