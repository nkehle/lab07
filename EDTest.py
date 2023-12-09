# Noa Kehle
# nkehle@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 07

import EditDistance
import sys

''' read the two lines individually '''
def read_single_file(filename):
    with open(filename, 'r') as file:
        string1 = file.readline().strip()
        string2 = file.readline().strip()

    return string1, string2

''' read the whole file at once '''
def read_multi_file(filename):
    with open(filename, 'r') as file:
        # read the entire file at once
        return file.read().strip()

'''
    Overview: Driver code for testing the ed with two files
    USAGE : python3 <EDTest.py> <file1> <file2 (optional)>
'''
if __name__ == "__main__":
    # check for one or two files given
    if len(sys.argv) == 2:
        string1, string2 = read_single_file(sys.argv[1])
    elif len(sys.argv) == 3:
        string1 = read_multi_file(sys.argv[1])
        string2 = read_multi_file(sys.argv[2])

    ed = EditDistance.EditDistance()
    distance = ed.findEditDistance(string1, string2)

    print(f"String1: {string1} ---- String2: {string2}")
    print(f"\nEDIT DISTANCE: {distance} with PATH of:\n")
    ed.recoverAlignment(string1, string2)
    