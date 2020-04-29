"""
Tests for geometry analysis functions.
"""

import geom_analysis as ga

def test_calculate_distance():
    coord1 = [0,0,0]
    coord2 = [1,0,0]

    expected = 1.0
    observed = ga.calculate_distance(coord1, coord2)

    assert observed == expected

def test_bond_distance_default():
    bond_d=1.0
    min_d=0.3
    max_d=0.7

    expected = False
    observed = ga.bond_check(bond_d,min_d,max_d)

    assert observed == expected

def test_bond_distance_1_5():
    
    bond_d=1.5
    
    expected = False
    observed = ga.bond_check(bond_d)

    assert observed == expected 
def test_bond_check_0():
    bond_distance = 0
    expected = False
    observed = ga.bond_check(bond_distance)

    assert expected == observed

def test_bon_check_1p6():
    bond_distance = 1.6
    expected = False
    observed = ga.bond_check(bond_distance)

    assert expected == observed

#Testing is particularly important for collaborative projects. Good to have a good test suite, with all tests needed to be satisfied for the code to run.
