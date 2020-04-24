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
	parser=argparse.ArgumentParser(description="This script parses amber mdout files to extract the total energy. You can also use it to create plots.")
	parser.add_argument("input_file",help="The filepath to the file to be analyzed.")
	args=parser.parse_args()
	path_full=args.input_file
	file_names=glob.glob(path_full)

	for path in file_names:
		lines=read_lines(path)
		output_file=open(os.path.basename(path).split('.')[0]+'_Etot.txt','w')
		output_file.write('Step\tEnergy\n')
		E=np.zeros(1000)
		n=0
		for i in lines:
			if ' R M S  F L U C T U A T I O N S' in i:
				break
			if 'NSTEP' in i:
				output_file.write(F'{i.split()[2]}\t')
			if 'Etot' in i:
				output_file.write(F'{i.split()[2]}\n')
				E[n]=float(i.split()[2])
				n+=1
		output_file.close()
		E=E[:n]
		plt.figure()
		plt.plot(E)
		plt.show()
