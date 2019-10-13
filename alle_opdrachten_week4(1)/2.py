#!/usr/bin/env python3
# Author: Carlijn Assen

import pickle
import sys
import numpy as np


def tf_idf_score():

    docs = pickle.load(open('docs.pickle', 'rb'))
    all_tweets = 0

    for line in sys.stdin:
        line = line.strip()
        [w1, w2] = line.split()

        term_in_document = 0

        for item in docs:
            all_tweets += 1
            words = docs[item][2].split()
            tweet_len = len(words)
            if w1 in words or w2 in words:
                term_in_document += 1
                w_occ = words.count(w1) + words.count(w2)

                tf = w_occ/tweet_len
                idf = np.log(all_tweets/term_in_document)
                tf_idf = tf * idf

                print('TF-IDF score: {0}'.format(tf_idf))
                print('Username: {0}'.format(docs[item][0]))
                print('Tweet: {0:>25}'.format(docs[item][1]))
                print()


tf_idf_score()
