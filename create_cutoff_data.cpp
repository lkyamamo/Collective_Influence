/*

file input is: ./cutoff_data.cpp file_name.adjlist cutoff_value

*/

#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <sstream>
#include <filesystem>    
    
int main(int argc, char* argv[]) {

    std::string CI_path = "/home/logan/Research/MediaNetworks/Collective_Influence";

    int cutoff = std::stoi(argv[2]);
    std::string inputString = argv[1];
    std::ifstream file_in(CI_path + "/raw_data/" + inputString);
    //gets the file name from the input
    std::string file_name = inputString.substr(0, inputString.find('.'));
    std::cout << CI_path + "/raw_data/" + file_name << std::endl;
    std::ofstream file_out("cutoff_data/" + file_name + "_cutoff_" + std::to_string(cutoff) + ".txt");
    
    std::string line;
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
            file_out << old_node1 << ' ' << old_node2;
            file_out << "\n";
        }
        
    }
    file_in.close();
    file_out.close();
}