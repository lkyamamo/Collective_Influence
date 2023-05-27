#this script processes all of the data that is in the raw_data folder and outputs files that are in the input format of "CI_HEAP"

#variables
cutoff_iteration_size=5
radial_increase=1


#create mapping for all data
tmpfile=$(mktemp)
python3 create_node_mapping.py > "$tmpfile"
N=$(cat "$tmpfile")
rm "$tmpfile"

#create mapped data according to cutoff parameter
# Specify the folder path
raw_data_folder="raw_data"

#Loop through different cutoff values
for ((i = 0; i <= 20; i += $cutoff_iteration_size)) do

    #loop through all files in the folder
    for file in "$raw_data_folder"/*; do
        if [[ -f "$file" ]]; then
            if [[ "$file" != "README.md" ]]; then
                ./convert_to_integer "$file" mapping.txt $i
            fi
        fi
    done
done

#convert all of the mapped data into CI_HEAP inputs
python3 create_integer_adjlist.py "$N"

input_folder="CI_Heap_input"
#with radial increase
for ((i = 1; i <= 3; i += radial_increase)) do
    for file in "$input_folder"/*; do
        if [[ "$file" != *"README.md" ]]; then
            ./CI "$file" "$i"
        fi
    done
done

#without radial increase
#for file in "$input_folder"/*; do
#    if [[ "$file" != "README.md"]]; then
#       ./CI "$file" 1
#    fi
#done

python3 results.py