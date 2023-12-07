# Noa Kehle
# nkehle@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 07

import numpy as np 

class EditDistance:
    def __init__(self):
        pass

    '''
        Overview: Given two string s and t, find the minimum edit distance
        Parameters:
            - string s
            - string t
        Return:
            - the minimum distance (int)
    '''
    def findEditDistance(self, s, t):
        # assign the lengths
        s_length = len(s)
        t_length = len(t)

        arr = np.zeros((s_length, t_length), dtype=int)

        # line the empty ones with 0
        for i in range(s_length):
            arr[i,0] = 0
        for j in range(1, t_length):
            arr[0,j] = 0

        for i in range(1, s_length):
            for j in range(1, t_length):
                if s[i] == t[j]:
                    arr[i,j] = arr[i-1, j-1]
                else:
                    arr[i,j] = min(arr[i-1, j],arr[i, j-1],arr[i-1, j-1])
        
        return arr[i,j]

    '''
        Overview: Given a solution to editdistance print out the path
        that was chosen to conver s to t
        Return:
            - print the path
    '''
    def recoverAllignment(self):
        pass
