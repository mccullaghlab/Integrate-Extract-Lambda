#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
import numpy as np
import sys

# NOTE command line input: ./integrate_extract_lambda.py Outputfile Inputfile Inputfile ... InputFile

# reads as many input log files as necessary
length = int(len(sys.argv))

if length is 1:
	print 'Usage: ./script OutputFile InputFile InputFile ... InputFile'
	print 'OutputFile = relevant information from namd log file extracted, as well as deltaA calculated'
	print 'InputFile = namd log file (Not Thermodynamic Integration output file)'
else: 
# write to file input after ./integrate_extract_lambda.py
	nf = open(sys.argv[1], 'w')
	nf.write(' stage   name      force      lambda0     lambda1  dA/dlambda \n')
# skip ./integrate_extract_lambda.py output, extract from every input following
	for i in range(2,length):
		d1 = sys.argv[i]
		print "Reading: %s" % d1
		data = open(d1, 'r')
	
		lambda0 = 0
		dAdl = 0
		name = None
		stage = 0
		lambda1 = 0
		force = 0
	
		for line in data:
			d = line.split()
			if "colvars:" in d:
			        if "Lambda=" in d:
				        lambda0 = float(d[2])
		        		dAdl = float(d[4])
			        if "Restraint" in d:
# NOTE prints harmonic name as number: removes inherent trailing comma, and removes first 8 letters of the name 
# for example, my name is 'harmonic##,', and I convert it to '##'
				        name = d[2]
					name = name[8:-1]
					name = float(name)
		        		stage = float(d[4])
				        lambda1 = float(d[8])
		        	if "Setting" in d: 
	       				force = float(d[5])
					nf.write('%4.0f  %6.0f  %10.4f  %10.4f  %10.4f  %10.4f \n' % (stage, name, force, lambda0, lambda1, dAdl))
	print "Output: %s" % sys.argv[1]
	nf.close()
# Integrate from 0 to 1 for all dA/dLambda values
	count = 0
	nf = open(sys.argv[1], 'r')
	runningInt = 0

	for line in nf:
		d = line.split()
		if count >= 2:
			dIn = float(d[5])
			runningInt += dIn
		count += 1
	nf.close
	nf = open(sys.argv[1], 'a')
	nf.write('\n deltaA: %10.4f' % (runningInt))
	print "deltaA: %f" % runningInt
