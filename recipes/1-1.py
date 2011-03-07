# Processing a string one character at a time

import com

theList = list(com.theStr)
print theList

for c in com.theStr:
    print c,

print
print '\''.join(c for c in com.theStr)
