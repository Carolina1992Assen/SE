#!/usr/bin/env python3
# Author: Carlijn Assen


from nltk.tokenize import TweetTokenizer, RegexpTokenizer
from itertools import permutations
from time import sleep
import numpy as np
import re
import math
import string
import pickle
from operator import itemgetter


def del_symbols(text):
    result = re.sub(r"[()+-.../#]", r"", text)
    return result


def del_emojis(text):
    return text.encode('ascii', 'ignore').decode('ascii')


def del_tw(text):
    result = re.sub(r"https\S+", "", text)
    return result


def del_rt(text):
    result = re.sub(r"RT", "", text)
    return result


def del_punct(s):
    result = s.translate(str.maketrans("", "", string.punctuation))
    return result


def highest_score():

    scores = pickle.load(open("data.pickle", "rb"))
    docs = pickle.load(open('docs.pickle', 'rb'))
    
    tw_tok = TweetTokenizer(preserve_case = False, strip_handles = True, reduce_len = True)
    
    perm_list = []
    term_in_doc = 0
    t_list = []
    values = []
    binary_list = []
    info_dict = {}
    
    for item in docs:
   
        words = docs[item][2]
        words = del_emojis(words)
        words = del_tw(words)
        words = del_symbols(words)
        words = del_punct(words)
        words = del_rt(words)
        words = tw_tok.tokenize(words)
        term_in_doc += 1

        perms = (permutations(words, 2))
    
        for i, j in perms:
            w1 = i
            w2 = j
        
        l1 = scores.get(w1, {})
        l2 = scores.get(w2, {})
      
    with open("info.pickle", "wb") as f:
        pickle.dump(info_dict, f)



def main():

    info = pickle.load(open("info.pickle", "rb"))
    print(sorted(info.items(), key=itemgetter(0)))
    
if __name__ == "__main__":
    main()
