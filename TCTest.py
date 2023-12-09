# Noa Kehle
# nkehle@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 07

import sys
import TestChecker  

'''
    Overview: read the contents of a file and strip whitespace
    Parameters:
        - filename
    Return:
        - contents of the file
'''
def read_dictionary_file(test_checker, filename):
    with open(filename, 'r') as file:
        dictionary_words = []
        # read one line of the file
        for line in file:
            dictionary_words.append(line.strip())
            
    test_checker.setDictionary(dictionary_words)
    return

'''
    Overview: Driver code for testing the TestChecker with two files
    USAGE : python3 <TCTest.py> <dictionary text file> <strings text file>
'''
if __name__ == "__main__":
    # make an instance of TestChecker
    test_checker = TestChecker.TestChecker()
    strings = []

    # set the dictionary
    read_dictionary_file(test_checker, sys.argv[1])       # dictionary file

    # go through each of the strings
    with open(sys.argv[2], 'r') as file:
        for line in file:
            strings.append(line.strip())
        
    # go through all the strings 
    for string in strings:
        test_checker.setString(string)
        # analyze the string
        if test_checker.isText():
            test_checker.split()
        else:
            print("String:", test_checker.string, "is not a text")
        
