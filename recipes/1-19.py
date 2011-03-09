# Checking a string for any of multiple endings

import itertools

def anyEnds(pred, seq):
    #return True in itertools.imap(pred, seq)
    return True in map(pred, seq)

def endsWith(s, *endings):
    return anyEnds(s.endswith, endings)

files = ['abc.jpg', 'def.txt', 'ghi.gif']

for fileName in files:
    if endsWith(fileName, '.jpg', '.gif'):
        print fileName

