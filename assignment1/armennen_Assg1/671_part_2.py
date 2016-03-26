import re
import nltk
from itertools import *
from nltk.probability import FreqDist, ConditionalFreqDist
from math import *

WORD_RE = re.compile(r"([A-Za-z]{1,5})")

FULLWORD_RE = re.compile(r"[\w ]+")
textlist=list()
wdict= dict()
text= open(r'enwiktionary.a.list','rU')
for a in text:
	#word= a.split()
	reword=WORD_RE.findall(a.lower())
	realword=FULLWORD_RE.findall(a.lower())
	for b in realword:
            wdict[b]=[a for a in reword]



def jaccardtest(a):
    #jaccard = 1 - (Count of shared trigrams)/(len(mispelled word)+len(dictionary word)) 
    splitword=WORD_RE.findall(a)  #splitting word into trigram
    testdic=dict()
    match=0
    #counter=0
    test1=list()
    

    for tri in splitword:
        test1.append(tri.lower())
    for wordkey,pieces in wdict.items():
        trlist=list()
        counter=0
        for frag in test1:
            for threeletterfragment in pieces:
                trlist.append(threeletterfragment)
                if frag[0]==threeletterfragment[0]:    			
                    counter+=1
                    if counter<2:
                        testdic[wordkey]=1
                    else:
                        testdic[wordkey]+=1

    for words,counts in testdic.items():
        x=splitword
        y=wdict[words]
        similarity = len(set.intersection(*[set(x), set(y)]))
        allcharac = len(set.union(*[set(x), set(y)]))
        jaccard= similarity/float(allcharac)
        testdic[words]=jaccard

    test1=list()
    for key, value in sorted(testdic.iteritems(), reverse=True, key=lambda (k,v): (v,k))[:10]:
        test1.append((key, value))
    return test1

print jaccardtest("agglumetation")

