This repository uses Makse's C implementation of his Collective Influence algorithm described in Makse 2016 Scientific Reports 30062. His code is CI_HEAP.c with minute changes made to clean up output file naming. 

to obtain results for the data, put the data in the raw_data folder, run "./process_raw_data.sh" and the results will be in the results folder. Make sure to fix bash script access permissions if necessary.
The results are going to be a ranking of nodes from most to least influencial. 
You can also change the increase in weight cutoff iteration value and limit along with the same values for the ball radius in the process_raw_data.sh script file variables at the top
