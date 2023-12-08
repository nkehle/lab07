# Noa Kehle
# nkehle@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 07

import numpy as np 

class EditDistance:
    # initialize to empty
    def __init__(self):
        self.matrix = None
        self.s = None
        self.t = None

    '''
        Overview: Given two string s and t, find the minimum edit distance
        Parameters:
            - string s
            - string t
        Return:
            - the minimum distance (int)
    '''
    def findEditDistance(self, s, t):
        self.s = s
        self.t = t
        # assign the lengths
        s_length = len(s)
        t_length = len(t)

        self.matrix = np.zeros((s_length + 1, t_length + 1), dtype=int)

        # init the first rows
        for i in range(s_length + 1):
            self.matrix[i, 0] = i
        for j in range(t_length + 1):
            self.matrix[0, j] = j

        # go through the entire matrix row by row
        for i in range(1, s_length + 1):
            for j in range(1, t_length + 1):
                if s[i - 1] == t[j - 1]:
                    self.matrix[i, j] = self.matrix[i - 1, j - 1]
                else:
                    self.matrix[i, j] = min(self.matrix[i - 1, j],          # deletion
                                            self.matrix[i, j - 1],          # addition
                                            self.matrix[i - 1, j - 1]) + 1  # replacement

        # return the bottom right corner
        return self.matrix[s_length, t_length]

    '''
        Overview: Given a solution to editdistance print out the path
        that was chosen to conver s to t
        Return:
            - print the path
    '''
    def recoverAlignment(self, s, t):
        i, j = len(s), len(t)
        path = []

        while i != 0 or j != 0:  # Use 'or' instead of '&'
            if i > 0 and j > 0 and s[i - 1] == t[j - 1]:
                path.append(f"Keep character '{s[i - 1]}' @ position {i}")
                i -= 1
                j -= 1
            else:
                if j == 0 or (i > 0 and self.matrix[i, j - 1] >= self.matrix[i - 1, j]):
                    path.append(f"Delete character '{s[i - 1]}' @ position {i}")
                    i -= 1
                else:
                    path.append(f"Insert character '{t[j - 1]}' @ position {i}")
                    j -= 1
        path.reverse()
        for move in path:
            print(move)


# driver code
ed = EditDistance()
s = "me"
t = "mee"
distance = ed.findEditDistance(s, t)
print("Edit Distance:", distance)
print("Matrix: \n", ed.matrix)
ed.recoverAlignment(s, t)
