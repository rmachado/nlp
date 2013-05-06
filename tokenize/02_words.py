'''
Created on 06/05/2013

@author: Rodrigo
'''

from nltk.tokenize import word_tokenize, PunktWordTokenizer, RegexpTokenizer
print word_tokenize("Hello word!")

print word_tokenize("We can't do this")

tokenizer = PunktWordTokenizer()
print tokenizer.tokenize("We can't do this")

tokenizer = RegexpTokenizer("[\w']+")
print tokenizer.tokenize("We can't do this")

# Split instead of findall
tokenizer = RegexpTokenizer("\s+", gaps=True)
print tokenizer.tokenize("We can't do this")
