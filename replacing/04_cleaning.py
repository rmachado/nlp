'''
Created on 08/05/2013

@author: Rodrigo
'''

from nltk.tokenize import word_tokenize
from helpers.replacers import RegexpReplacer, RepeatReplacer

texts = ["Can't is a contraaaaction",
         "I sshould've done that thing I didn't dooooo",
         "This boomerang ain't very effective"]         

regex_repl = RegexpReplacer()
repeat_repl = RepeatReplacer()

for text in texts:
    text = regex_repl.replace(text)
    print [repeat_repl.replace(w) for w in word_tokenize(text)]
    