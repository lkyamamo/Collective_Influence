#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <sstream>

int main(){
    std::string str = "/home/lkyamamoto/Research/MediaNetworks/CI_algorithm/raw_data/network_original_comm.adjlist";

    size_t begin = str.find_last_of('/') + 1;
    size_t last = str.find_last_of('.');

    size_t length = last - begin;

    std::cout << str.substr(begin, length) << std::endl;
}
