/*

This file will loop through all files in "raw_data" folder, find their associated integer mapping file in the 
"maps" folder, and output an integer mapped integer edge list with specified cutoff value into the "mapped_data" folder

*/

#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <sstream>
#include <filesystem>

//command line input will be ./convert_to_integer input_file.txt map_file.txt


int main(int argc, char* argv[]) {
    std::string CI_path = "/home/logan/Research/MediaNetworks/Collective_Influence";
    std::string cutoff_data_path = CI_path + "/cutoff_data";

    std::ifstream file_in(cutoff_data_path + "/" + argv[1]);
    std::ifstream mapping(CI_path + "/maps/" + argv[2]);
    std::cout << CI_path + "/maps/" + argv[2] << std::endl;

    std::string inputString = argv[1];
    std::string fileName = inputString.substr(0, inputString.find('.'));
    if (fileName.substr(fileName.length() - 3) != ".md") {
        //getting output file name
        std::string file_name = fileName;
        size_t begin = file_name.find_last_of('/') + 1;
        size_t last = file_name.find_last_of('.');

        size_t length = last - begin;
        file_name = file_name.substr(begin,length);

        //eliminating the network_ and _comm
        begin = file_name.find_first_of('_') + 1;
        last = file_name.find_last_of('_');
        length = last-begin;

        file_name = file_name.substr(begin,length);

        //get mapping file
        std::ifstream mapping_file(CI_path + "/maps/" + file_name + "_mapping.txt");

        if(!mapping_file){
            std::cout << "could not open map file" << std::endl;
        }

        //create map from mapping file

        std::string line;
        std::map<std::string, std::string> node_map;

        // Read each line in and add the key value pair to the map
        while (std::getline(mapping_file, line)) {
            std::stringstream ss(line);
            std::string key;
            std::string value;

            ss >> key;
            ss >> value;

            node_map.insert(std::make_pair(key, value));


        }
        mapping_file.close();

        //create the new output file that will be the integer mapped version of the raw data
        std::string old_node1, old_node2;

        std::ofstream file_out("mapped_data/" + file_name + "_integer_unweighted" + ".txt");
        // Read lines from the file one by one
        while (std::getline(file_in, line)) {
            std::stringstream ss(line);

            //get the nodes from the edge and write the mapped node values to the output file
            ss >> old_node1;
            ss >> old_node2;
            
        }
        file_in.close();
        file_out.close();
    }
}
