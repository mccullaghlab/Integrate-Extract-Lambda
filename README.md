#Extract and Integrate Lambda data from NAMD log 
When running NAMD with targetNumStages to change a COLVAR over time, lambda values, force constants, and dA/dLambda will be stored in the NAMD log files. Running this script will extract all of these relevant values for each harmonic constraint into a data file, sorted by stages.
Additionally, it will perform an integration over all harmonic constraints from lambda 0 to 1.

#Usage:
Everything is specified in the command line. Output file (sample: lambda1.dat), and input files (sample: run#.log) 

> ./script Outputfile Inputfile … Inputfile
