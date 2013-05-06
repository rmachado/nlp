'''
Created on 06/05/2013

@author: Rodrigo
'''

from nltk.corpus import stopwords, RegexpTokenizer
english_stops = set(stopwords.words('english'))
tokenizer = RegexpTokenizer('\s+', gaps=True)
print [w for w in tokenizer.tokenize("This is not a common book") if not w in english_stops]
