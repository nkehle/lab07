# Noa Kehle
# nkehle@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 07

import EditDistance
import sys

'''
    Overview: read the contents of a file and strip whitespace
    Parameters:
        - filename
    Return:
        - contents of the file
'''
def read_file(filename):
    with open(filename, 'r') as file:
        # read the entire file at once
        file_content = file.read()
        # remove the newline chars and whitspace        
        stripped_content = file_content.strip()

    return stripped_content

'''
    Overview: Driver code for testing the ed with two files
'''
if __name__ == "__main__":
    # check the input (shouldn't be wrong with grader)
    if len(sys.argv) != 3:
        print("Incorrect file input")
        sys.exit(1)

    # read the contents into vars
    file1_content = read_file(sys.argv[1])
    file2_content = read_file(sys.argv[2])

    ed = EditDistance()
    distance = ed.findEditDistance(file1_content, file2_content)

    print(f"Edit Distance: {distance}")
    print("Path Chosen:")
    ed.recoverAlignment(file1_content, file2_content)
    