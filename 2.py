#!/usr/bin/env python3
# Author: Carlijn Assen

import pickle
import sys
import numpy as np


def tfidf(w1, w2):

    docs = pickle.load(open('docs.pickle', 'rb'))
    all_words = pickle.load(open('words_index.pickle', 'rb'))
    all_words = list(all_words.keys())
    all_tweets = 0
    tf_idf_scores = {}
    
    
    for item in docs:
        all_tweets += 1
        words = docs[item][2].split()
        tweet_len = len(words)
        term_in_document2 = 0
        try:
            if w1 in words:
                term_in_document += 1
                w_occ = words.count(w1)
                tf = w_occ/tweet_len
                df = term_in_document/all_tweets
                idf = np.log(all_tweets/df)
                tf_idf = tf * idf
            else:
                tf_idf = 1
            if w2 in words:
                term_in_document2 += 1
                w_occ2 = words.count(w2)
                tf2 = w_occ2/tweet_len
                df2 = term_in_document2/all_tweets
                idf2 = np.log(all_tweets/df2)
                tf_idf2 = tf2 * idf2
            else:
                tf_idf2 = 1
           
            tf_idf_scores[all_tweets] = [tf_idf, tf_idf2]
        
            
        except KeyError:
            print('try another query', file=sys.stderr)
          

    with open('ti_scores.pickle', 'wb') as f:
        pickle.dump(tf_idf_scores, f)
            
                   
     
print(tfidf('hallo', 'ik'))          
           



