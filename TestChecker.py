# Noa Kehle
# nkehle@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 07


class TestChecker:
    '''
        Overview: initializes an instanc ef TestChecker
    '''
    def __init__(self):
        self.string = None
        self.dictionary = set()
        self.istext = False

    '''
        Overview: returns if substring from i to j is in dict
        Parameters:
            - i and j
        Return:
            - true if in dictionary
    '''
    def dict(self, i, j):
        substring = self.string[i:j]
        return substring in self.dictionary

    '''
        Overview: sets the TestChecker instance dictionary 
        Parameters:
            - input list of words
    '''
    def setDictionary(self, dictionary):
        self.dictionary = set(dictionary)
    
    '''
        Overview: sets the TestChecker instance dictionary 
        Parameters:
            - string s
    '''
    def setString(self, s):
        self.string = s
    
    '''
        Overview: determines if the text is made up of only 
        substrings in the dictionary
    '''
    def isText(self):
        n = len(self.string)
        arr = [False] * (n + 1)
        arr[0] = True  # emptry string is valid

        for i in range(1, n + 1):
            for j in range(i, 0, -1):
                if self.dict(j - 1, i) and arr[j - 1]:
                    arr[i] = True
                    break

        self.istext = arr[n]
        return self.istext
    
    '''
        Overview: recovers the words that make up the split and prints
    '''
    def split(self):
        if not self.istext:
            print("The string ", self.string, " is not a text")
            return

        n = len(self.string)
        split_result = self.find_split(0, n)

        # Print the split
        print("String:", self.string, " splits into the words:", split_result)

    '''
    Overview: recursively identifies a valid split of the input string into dictionary words
    '''
    def find_split(self, start, end):
        if start == end:
            return []

        for i in range(start + 1, end + 1):
            if self.dict(start, i):
                rest_of_split = self.find_split(i, end)
                if rest_of_split is not None:
                    return [self.string[start:i]] + rest_of_split

        return None



        
