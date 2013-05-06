'''
Created on 06/05/2013

@author: Rodrigo
'''

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print lemmatizer.lemmatize('cooking')
print lemmatizer.lemmatize('cooking', pos='v') # Verb
print lemmatizer.lemmatize('cookbooks')

""" Difference between stemming and lemmatization """
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print stemmer.stem("believes")
print lemmatizer.lemmatize("believes")