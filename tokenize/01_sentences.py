'''
Created on 03/05/2013

@author: Rodrigo
'''

# Simple sentence tokenize

from nltk.tokenize import sent_tokenize
para = "Hello World. It's good to see you. Thanks for buying this book."
print sent_tokenize(para)

# The instance used in sent_tokenize() is actually loaded on demand from a pickle
# file. So if you're going to be tokenizing a lot of sentences, it's more efficient to load the
# PunktSentenceTokenizer once, and call its tokenize() method instead

from time import time

list = [para] * 1000
start = time()
for elem in list:
    sent_tokenize(elem)
print "Using different instances: " + str(time() - start)

import nltk.data
tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")

start = time()
for elem in list:
    tokenizer.tokenize(elem)
print "Using the same instance: " + str(time() - start)

# Other languages
spanish_tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
print spanish_tokenizer.tokenize('Hola mundo. Que bueno verlos. Gracias por comprar este libro.')

