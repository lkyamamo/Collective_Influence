#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <sstream>

//command line input will be ./convert_to_integer input.txt mapping.txt cutoff_value

int main(int argc, char* argv[]) {
    std::ifstream file_in(argv[1]);
    std::ifstream mapping(argv[2]);
    int cutoff = std::stoi(argv[3]);

    //getting output file name
    std::string file_name = argv[1];
    size_t begin = file_name.find_last_of('/') + 1;
    size_t last = file_name.find_last_of('.');

    size_t length = last - begin;
    file_name = file_name.substr(begin,length);

    //eliminating the network_ and _comm
    begin = file_name.find_first_of('_') + 1;
    last = file_name.find_last_of('_');
    length = last-begin;

    file_name = file_name.substr(begin,length);

    

    std::ofstream file_out("mapped_data/" + file_name + "_cutoff_" + std::to_string(cutoff) + "_integer_unweighted" + ".txt");

    // Check if we successfully opened the files
    if (!mapping || !file_out) {
        std::cerr << "Unable to open input file";
        return 1;   // Return with error code
    }

    if (!mapping) {
        std::cerr << "Unable to open mapping file";
        return 1;   // Return with error code
    }

    //create map from mapping file

    std::string line;
    std::map<std::string, std::string> node_map;

    // Read each line in and add the key value pair to the map
    while (std::getline(mapping, line)) {
        std::stringstream ss(line);
        std::string key;
        std::string value;

        ss >> key;
        ss >> value;

        node_map.insert(std::make_pair(key, value));


    }

    //create the new output file that will be the integer mapped version of the raw data
    std::string old_node1, old_node2, weight;
    std::string new_word;  

    // Read lines from the file one by one
    while (std::getline(file_in, line)) {
        std::stringstream ss(line);

        //get the nodes from the edge and write the mapped node values to the output file
        ss >> old_node1;
        ss >> old_node2;
        ss >> weight;
        
        //with cutoffs
        
        if(std::stoi(weight) > cutoff){
            file_out << node_map[old_node1] << ' ' << node_map[old_node2];
            file_out << "\n";
        }
        

        //without cutoffs
        //file_out << node_map[old_node1] << ' ' << node_map[old_node2];
        //file_out << "\n";
    }

    file_in.close();
    file_out.close();

    return 0;
}
