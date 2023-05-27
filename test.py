import os

my_dict = {}

my_dict[1] = [2,3,4]
my_dict[2] = [4,5,6]

try:
    my_dict[3]
except KeyError:
    my_dict[3] = []

with open("output.txt", "w") as f:

    for key, values in my_dict.items():

        #write first node
        f.write("{0} ".format(key))

        #write neighbors
        for element in values:
            f.write("{0} ".format(element))
        f.write("\n")