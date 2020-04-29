import os
import argparse
import glob
import matplotlib.pyplot as plt
import numpy as np


def read_lines(path):
	"""
	Function that reads in file and output a list of all lines of the file.
	Input: File path.
	Return: List with all lines of the file.
	"""
	f=open(path,'r')
	lines=f.readlines()
	f.close()
	return lines

if __name__=='__main__':
	#Define the argument parser and what arguments it should parse.
	parser=argparse.ArgumentParser(description="This script parses amber mdout files to extract the total energy. You can also use it to create plots.")
	parser.add_argument("input_file",help="The filepath to the file to be analyzed.",nargs='*')
	#could use nargs='*' and not need to have path in string
	parser.add_argument("-plot_check",help="Tag to check whether the user wants a plot.",action='store_true')
	#Get the arguments.
	args=parser.parse_args()
	#Get all the filenames.
	#path_full=args.input_file
	#file_names=glob.glob(path_full)
	file_names=args.input_file
    #Check if should plot the results.
	plot_check=args.plot_check

	#Loop over all files.
	for path in file_names:
		#Read in file lines.
		lines=read_lines(path)
		file_name=os.path.basename(path).split('.')[0]
		#Create output file and write headers.
		output_file=open(file_name+'_Etot.txt','w')
		output_file.write('Step\tEnergy\n')
		#Arrays to store the step number and energies for plotting.
		E=np.zeros(10000)
		NSTEPS=np.zeros(10000)
		#Dummy variable to check the size of the arrays.
		n=0
		#Loop over lines as in exercise 1.
		for i in lines:
			#Stops the loop when reach the RMS values.
			if ' R M S  F L U C T U A T I O N S' in i:
				break
			if 'NSTEP' in i:
				output_file.write(F'{i.split()[2]}\t')
				NSTEPS[n]=float(i.split()[2])
			if 'Etot' in i:
				output_file.write(F'{i.split()[2]}\n')
				E[n]=float(i.split()[2])
				n+=1
		output_file.close()
		NSTEPS=NSTEPS[:n]
		E=E[:n]
		#Check if user wants to plot the energies.
		if plot_check is True:
			plt.figure()
			plt.xlabel('Number of Steps')
			plt.ylabel('Energy ')
			plt.plot(NSTEPS,E)
			plt.savefig(file_name+'.png')
			#plt.show()
