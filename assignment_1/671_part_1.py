#Calculate bigram frequencies across all documents
import re
import nltk
from nltk.collocations import *
import math
from math import *
import numpy as np
from nltk.tokenize import TweetTokenizer
import csv

tweezer=TweetTokenizer(preserve_case=False, strip_handles=True)
f=open(r'tweets.txt','rU')
WORD_RE = re.compile(r"\b([A-Za-z'-]+)\b")
tweet_phrases=[]
melist=[]

for a in f:
    wordfilter=WORD_RE.findall(a)
    tweet_phrases.extend(wordfilter)
    #melist.append(wordfilter)
    bigramstogether=zip(WORD_RE.findall(a), WORD_RE.findall(a)[1:])
        #key=str(c) +' '+str(b)
    melist.extend(bigramstogether)

#print len(melist)

bigram_count=dict(nltk.FreqDist(melist))

#print bigram_count
#6641958
#UNIGRAMS
unigram_count = dict(nltk.FreqDist(tweet_phrases))


#finding the total number of unigrams in the text
    #TOTAL UNIGRAMS: 7615209
#print sum(unigram_count.values())

print len(unigram_count.keys())


# PMI#
def PMI(big, unig):
    probs = []
    for x in big:
        print unig[x[0]]
        p = math.log((float(big[x])/6641958)/((float(unig[x[0]])/7615209)*(float(unig[x[1]])/7615209)), 2)
        s = [x, p, big[x], unig[x[0]], unig[x[1]]]
        probs.append(s)
    psort = sorted(probs, key = lambda x:x[1], reverse=True)
    with open('pmi.csv', 'wb') as f:
        w = csv.writer(f)
        w.writerow(["Bigram", "Pointwise Coefficient", "(x,y)", "(x)", "(y)"])
        for x in range(0, 99):
            w.writerow(psort[x])
    return psort[0:99]
#print PMI(bigram_count, unigram_count)

# #MI CALC
# def computeMI(x, y):

#         sum_mi = 0.0
#         x_value_list = np.unique(x)
#         y_value_list = np.unique(y)
#         Px = np.array([ len(x[x==xval])/float(len(x)) for xval in x_value_list ]) #P(x)
#         Py = np.array([ len(y[y==yval])/float(len(y)) for yval in y_value_list ]) #P(y)
#         for i in xrange(len(x_value_list)):
#             if Px[i] ==0.:
#                 continue
#             sy = y[x == x_value_list[i]]
#             if len(sy)== 0:
#                 continue
#             pxy = np.array([len(sy[sy==yval])/float(len(y))  for yval in y_value_list]) #p(x,y)
#             t = pxy[Py>0.]/Py[Py>0.] /Px[i] # log(P(x,y)/( P(x)*P(y))
#             sum_mi += sum(pxy[t>0]*np.log2( t[t>0]) ) # sum ( P(x,y)* log(P(x,y)/( P(x)*P(y)) )
#         return x

#print computeMI(tweets)

#props to Peter Eldred
def chi(bi, uni):
    probs = []
    for x in bi:
        p = ((float(bi[x])/6641958)-(float(uni[x[0]]/7615209)*float(uni[x[1]]/7615209)))**2/((float(uni[x[0]])/7615209)*(float(uni[x[1]])/7330952))
        s = [x, p, bi[x], uni[x[0]], uni[x[1]]]
        probs.append(s)
    psort = sorted(probs, key = lambda x:x[1], reverse=True)
    with open('chisquare.csv', 'wb') as f:
        w = csv.writer(f)
        w.writerow(["Bigram", "Chi Square Coefficient", "(x,y)", "(x)", "(y)"])
        for x in range(0, 99):
            w.writerow(psort[x])
    return psort[0:99]
#print chi(bigram_count, unigram_count)

def MI(bi, uni):
    probs = []
    for x in bi:
        p = (float(bi[x])/6641958)*(math.log((float(bi[x])/6641958)/((float(uni[x[0]])/7615209)*(float(uni[x[1]])/7615209)), 2))
        s = [x, p, bi[x], uni[x[0]], uni[x[1]]]
        probs.append(s)
    psort = sorted(probs, key = lambda x:x[1], reverse=True)
    with open('mi.csv', 'wb') as f:
        w = csv.writer(f)
        w.writerow(["Bigram", "MI Coefficient", "(x,y)", "(x)", "(y)"])
        for x in range(0, 99):
            w.writerow(psort[x])
    return psort[0:99]
#print MI(bigram_count, unigram_count)
