import os
import re


#top = 10 #change to see however many top influencers you want
start_line = 8 #from structure of file

collective_influence = os.getcwd()

influencer_ranking_path = collective_influence + "/Influencer_ranking"
results_path = collective_influence + "/results/"

#create mapping from mapping.txt file
mapping = {}
with open(collective_influence + "/mapping.txt", "r") as f:
    for line in f:
        values = line.split(' ')
        mapping[int(values[1])] = values[0]

#loop over all files
for file in os.scandir(influencer_ranking_path):
    if(file.name[-2:] != "md"):

        #map back to original integer value
        file_path = collective_influence + "/secondary_mapping/" + (file.name.split()[0])[12:-10] + ".txt"
        secondary_mapping = {}
        with open(file_path, "r") as f:
            for line in f:
                values = line.split(' ')
                secondary_mapping[int(values[1])] = values[0]

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
                    numbers[1] = mapping[int(secondary_mapping[numbers[1]])]
                    results_file.write(f"{numbers[0]} \t {numbers[1]} \t {numbers[2]} \t {numbers[3]} \n")
