update 06/09/2023
note:
implementation before commit 5b325485af1084f98451a98259409d0811d1fee7 adapted a multiplex approach to a uniplex and as a result necessitated the use of two node mappings.
Implementation after commit ____ uses single mapping and should slightly increase performance on larger scale networks.

to obtain results for the data, put the data in the raw_data folder, run "./process_raw_data.sh" and the results will be in the results folder. Make sure to fix bash script access permissions if necessary.
The results are going to be a ranking of nodes from most to least influencial. 
You can also change the increase in weight cutoff iteration value and limit along with the same values for the ball radius in the process_raw_data.sh script file variables at the top

***IMPORTANT***
it is necessary that the input name of the raw_data files be of the format "network_<description>_comm.adjlist"
Contact me if further explanation is needed