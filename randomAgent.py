'''
author: ajaypanthagani
language: python 3
pre-requisites:
1. numpy library
2. text file containing user agent string
'''
import numpy as np

#defining getUA function
def getUA():
    #declaring an empty result string
    random_ua = ''
    #defining the string having the text file's name
    ua_file = 'ua_file.txt'
    #exception handling code to prevent running into errors
    try:
        #opening the text file having the user agent strings as f
        with open(ua_file) as f:
            #reading all the lines in the file
            lines = f.readlines()
        #checking for number of files, if number of files > 0 true
        if len(lines) > 0:
            #declaring a random state object using numpy
            prng = np.random.RandomState()
            #generating a unique and random permutation
            index = prng.permutation(len(lines) - 1)
            #creating a random index
            idx = np.asarray(index, dtype=np.integer)[0]
            #retrieve a random user agent sting using the random index from the list of lines
            random_proxy = lines[int(idx)]
    except Exception as ex:
        print('Exception in random_ua')
        print(str(ex))
    #returning the random user agent string
    finally:
        return random_ua
