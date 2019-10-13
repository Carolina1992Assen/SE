#!/usr/bin/env python3
# Author: Carlijn Assen

import sys
import pickle 

from itertools import permutations

   
def highest_score():

    scores = pickle.load(open("data.pickle", "rb"))
    all_words = pickle.load(open("words_index.pickle", "rb"))
    
    perms_dict = {}
    
    words = list(all_words.keys())
    perms = (permutations(words, 2))
    for p in perms:
        print(p)

            
highest_score()


