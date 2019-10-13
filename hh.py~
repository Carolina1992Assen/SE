#!/usr/bin/env python3
# Author: Carlijn Assen

import sys
import pickle
import numpy as np

from operator import itemgetter


def tfidf():

    docs = pickle.load(open("docs.pickle", "rb"))
    all_words = pickle.load(open("words_index.pickle", "rb"))
    term_in_doc = 0
    d = {}
    data = defaultdict(dict)
    id_database = {}

    for word in all_words.keys():
        idds = all_words[word].keys()

        term_in_doc += 1
        data[word] = {}

        for item in idds:
            tweet = docs[item][2].split()
            occ = tweet.count(word)
            len_tweet = len(tweet)
            user = docs[item][0]
            text_tweet = docs[item][1]
            tf = occ / len_tweet
            df = term_in_doc / len(docs.keys())
            idf = np.log(len(docs.keys()) / df)
            tf_idf = tf * idf
            data[word][item] = (tf_idf, user, text_tweet)

    with open("data.pickle", "wb") as f:
        pickle.dump(data, f)


def main():
    scores = pickle.load(open("data.pickle", "rb"))
    for line in sys.stdin:
        line = line.strip()
        line = line.split()

        w1 = line[0]
        w2 = line[1]

        l1 = scores.get(w1, {})
        l2 = scores.get(w2, {})

        matches = {}

        if w1 not in scores.keys() and w2 not in scores.keys():
            print("Please, enter another Query!")
        elif w1 in scores.keys() and w2 not in scores.keys():
            for idd, tup in sorted(l1.items(), key=itemgetter(1), reverse=True):
                print(
                    "Word = {0}\nTF-IDF score = {1}\nUser = {2}\nTweet-text = {3}\n\n".format(
                        w1, tup[0], tup[1], tup[2]
                    )
                )

        elif w2 in scores.keys() and w1 not in scores.keys():
            for idd, tup in sorted(l2.items(), key=itemgetter(1), reverse=True):
                print(
                    "Word = {0}\nTF-IDF score = {1}\nUser = {2}\nTweet-text = {3}\n\n".format(
                        w2, tup[0], tup[1], tup[2]
                    )
                )

        elif w1 in scores.keys() and w2 in scores.keys():
            for idd in l1.keys() & l2.keys():
                score = l1[idd][0] * l2[idd][0]
                matches[idd] = (score, l1[idd][1], l1[idd][2])
            for idd, tup in sorted(matches.items(), key=itemgetter(1), reverse=True):
                print(
                    "Words = {0} & {1}\nTF-IDF score = {2}\nUser = {3}\nTweet-text = {4}\n\n".format(
                        w1, w2, tup[0], tup[1], tup[2]
                    )
                )


if __name__ == "__main__":
    main()
