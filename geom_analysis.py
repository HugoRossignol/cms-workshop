"""
Change to the file
"""

import numpy as np
import os
import argparse

def calculate_distance(atom1_coord, atom2_coord):
    """
    Calculates distance between two points in 3D space.
    Inputs: coordinates of two atoms
    Return: distance between the atoms
    """
    x_distance = atom1_coord[0] - atom2_coord[0]
    y_distance = atom1_coord[1] - atom2_coord[1]
    z_distance = atom1_coord[2] - atom2_coord[2]
    distance = np.sqrt(x_distance**2+y_distance**2+z_distance**2)
    return distance
def open_xyz(file_path):
    """
    Opens xyz file, seperates coordinates and symbols and recasts the coordinates as floats.
    """
    xyz_file=np.genfromtxt(file_path,skip_header=2,dtype='unicode')
    symbols=xyz_file[:,0]
    coordinates=xyz_file[:,1:]
    coordinates=coordinates.astype(np.float)
    return symbols, coordinates
def bond_check(distance,min_bond=0,max_bond=1.5):
    if distance > min_bond and distance < max_bond:
        return True
    else:
        return False

#Tell python this is main part of the code.
if __name__=='__main__':
    #Run command line python geom_analysis.py -h
    parser = argparse.ArgumentParser(description='The script analyzes a user given xyz file and outputs the length of the bonds.')
    parser.add_argument('xyz_file',help="The filepath for the xyz file to analyse.")
    parser.add_argument('-minimum_bond',help="Input minimum bond length",type=float,default=0)
    parser.add_argument('-maximum_bond',help="Input maximum bond length",type=float,default=1.5)

    args=parser.parse_args()
    #path_file=os.path.join('data','water.xyz')
    path_file = args.xyz_file
    symbols,coordinates=open_xyz(path_file)
    num_atoms = len(symbols)
    for num1 in range(0,num_atoms):
        for num2 in range(0,num_atoms):
            if num1>num2:
                distance=calculate_distance(coordinates[num1],coordinates[num2])
                #print 3 after the dot: :.3f
                if bond_check(distance,min_bond=args.minimum_bond,max_bond=args.maximum_bond) is True:
                    print(F'{symbols[num1]} to {symbols[num2]} : {distance:.3f}')
