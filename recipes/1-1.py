# Processing a string one character at a time

import lib

theList = list(lib.theStr)
print theList

for c in lib.theStr:
    print c,

print
print '\''.join(c for c in lib.theStr)
