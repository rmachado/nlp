'''
Created on 06/05/2013

@author: Rodrigo
'''

from nltk.stem import PorterStemmer, LancasterStemmer, RegexpStemmer, SnowballStemmer

words = ['cooking','cookery','flying']
sp_words = ['cocinando', 'cocinar', 'volando', 'volar']

def stem_test(stemmer, words):
    print '{:*^50}'.format('Testing ' + type(stemmer).__name__)
    for w in words:
        print w + " -> " + stemmer.stem(w)
    print ''


stem_test(PorterStemmer(), words)

stem_test(LancasterStemmer(), words)

stem_test(RegexpStemmer('ing$'), words)

""" SnowballStemmer supports 13 non-English languages """
stem_test(SnowballStemmer('spanish'), sp_words)
