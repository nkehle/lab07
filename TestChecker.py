# Noa Kehle
# nkehle@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 07


class TestChecker:
    def __init__(self):
        self.string = None
        self.dictionary = set()
        self.istext = False
    
    def dict(self, i, j):
        substring = self.string[i:j]
        return substring in self.dictionary

    def setDictionary(self, dictionary):
        self.dictionary = set(dictionary)

    def setString(self, s):
        self.string = s
    
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
    
    def split(self):
        pass


dictionary_words = {
    'i': True,
    'item': True,
    'am': True,
    'sam': True,
    'ma': True,
    'red': True,
    'dare': True,
    'rare': True,
    're': True,
    'in': True,
    'into': True,
    'to': True,
    'a': True,
    'the': True,
    '2': True,
    'main': True,
    'and': True,
    'an': True,
}
words_to_check = [
    "samiam",
    "iamsam",
    "iamiamiam",
    "maiamsam",
    "iteminred",
    "themainitemandtherarereddare",
    "itemandtheraredare",
    "maintothered",
    "redare",
    "reddare",
    "rareanddare",
    "redandrareinmain",
    "themaindare",
    "aandb",
    "intotooandthe",
    "themainsambutnotthelastone",
    "stop",
    "iamtired",
    "redraredareinannitem",
]

check = TestChecker()
check.setDictionary(dictionary_words)

for word in words_to_check:
    check.string = word
    result = check.isText()
    print(f"{word}: {result}")


        

        
