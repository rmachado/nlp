'''
Created on 06/05/2013

@author: Rodrigo
'''

""" Bigrams """
from nltk.corpus import webtext, stopwords
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

stopset = set(stopwords.words('english'))
filter_stops = lambda w: len(w) < 3 or w in stopset

words = [w.lower() for w in webtext.words('grail.txt')]
bcf = BigramCollocationFinder.from_words(words)
bcf.apply_word_filter(filter_stops)
print bcf.nbest(BigramAssocMeasures.likelihood_ratio, 5)

""" Trigrams """
from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures

words = [w.lower() for w in webtext.words('singles.txt')]
tcf = TrigramCollocationFinder.from_words(words)
tcf.apply_word_filter(filter_stops)
tcf.apply_freq_filter(3)
print tcf.nbest(TrigramAssocMeasures.likelihood_ratio, 5)