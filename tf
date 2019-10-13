#!/usr/bin/env python3
# Author: Carlijn Assen

import pickle
import sys
import numpy as np


def tfidf():

    docs = pickle.load(open('docs.pickle', 'rb'))
    all_words = pickle.load(open('words_index.pickle', 'rb'))
    term_in_doc = 0
    tf_idf_database = defaultdict(
    for word in all_words.keys():
        idds = all_words[word].keys()
        term_in_doc += 1
        for item in idds:
            tweet = docs[item][2].split()
            occ = tweet.count(word)
            len_tweet = len(tweet)
        tf = occ/len_tweet
        df = term_in_doc/len(docs.keys())
        idf = np.log(len(docs.keys())/df)
        tf_idf = tf * idf
        tf_idf_database[word] = tf_idf
            
            
    with open('tf_idf_scores.pickle', 'wb') as f:
        pickle.dump(tf_idf_database, f)
	

tfidf()         
         
def main():
    
    td_idf_scores = pickle.load(open('tf_idf_scores.pickle', 'rb'))
    docs = pickle.load(open('docs.pickle', 'rb'))
    all_words = pickle.load(open('words_index.pickle', 'rb'))
    for line in sys.stdin:
        line = line.strip()
        line = line.split()
        w1 = line[0]
        w2 = line[1]
        try:
            matches = all_words[w1].keys() & all_words[w2].keys()
            if matches:
                for item in matches:
                    print(tf_idf_database[w1][0])
        except KeyError:
            print('Try another Query!')

main()
                
            
            
        
           
  



