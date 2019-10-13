
#!/usr/bin/env python3

import numpy as np
import pickle
import sys
from operator import itemgetter
def intersect(alist, blist):
    it1 = iter(alist)
    it2 = iter(blist)
    sol = []

    n1 = next(it1)
    n2 = next(it2)
    while True:
        try:
            if n1 == n2:
                sol.append(n1)
                n1 = next(it1)
                n2 = next(it2)
            else:
                if n1 < n2:
                    n1 = next(it1)
                else:
                    n2 = next(it2)
        except StopIteration:
            return sol
            
def data_collection():

    database = {}
    idd ={}
    # [term] --> [id_tag, total_docs, amount of docs term occurs in, amount term occurs in specic tweet]
    # [tweet_id] --> (user, text)
    total_docs = 0
    for line in sys.stdin:
        total_docs = total_docs + 1
        [id_tag, user, text, terms] = line.rstrip().split('\t')
        terms = terms.rstrip().split()
        l = 0
        for item in terms:
            idd = {}
            occ_tw = terms.count(item)
            idd[id_tag] = [[occ_tw], [user], [text], [len(terms)]]
            if item not in database.keys():
                database[item] = [[idd], [id_tag]]
            elif item in database.keys():
                database[item][0].append(idd)
                database[item][1].append(id_tag)
              
                
    for k, v in database.items():
        database[k].insert(1, total_docs)
        database[k].insert(-2, len(database[k][-1]))        
       
    with open('data.pickle', 'wb') as f:
        pickle.dump(database, f)
    #word ==> (dict[id] --> {[[occ_tweet, user, text, len_tweet]occ_doc]]}]total_doc, [list of tweets]]

def calculate_tf_idf(query):
    data = pickle.load(open('data.pickle', 'rb'))
    print(data.items())
    '''if len(query) > 1:
     
        w1 = query[0]
        w2 = query[1]
        
        w1_ids = set(data[w1][-1])
        w2_ids = set(data[w2][-1])
        
        matches = set(w1_ids & w2_ids)
        print(matches)
   
        for k, v in data.items():
            id_s = v[0][0].keys()
            if id_s in matches:
                priint(id_s)
          
                
       
        
        a = set(data[w1][0])
        b = set(data[w2][0])
        print(a)
        print('\n\n\n\n')
        print(b)
        print(a & b)'''
                
     
calculate_tf_idf(['en', 'ook'])
    
        
'''def check_for_existance(w):
    data = pickle.load(open('data.pickle', 'rb'))
    words_database = data.keys()
    if w in words_database:
        return True
    else:
        return False
    

def main():
    for line in sys.stdin:
        line = line.rstrip()
        line = line.split()
        w1 = line[0]
        w2 = line[1]
        if check_for_existance(w1) and check_for_existance(w2):
            print(calculate_tf_idf([w1,w2]))
main()'''

   
            
            

    
        
        
