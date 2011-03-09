# Reversing a string by words or characters

import lib
import re

print lib.theStr[::-1]

theList = lib.theStr.split()
theList.reverse()
print theList

aStr = 'This is  Tom Cat,   That   is Garfield.'
aList = re.split(r'\s+', aStr)
print ' '.join(reversed(aList))
