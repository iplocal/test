# Reversing a string by words or characters

import com
import re

print com.theStr[::-1]

theList = com.theStr.split()
theList.reverse()
print theList

aStr = 'This is  Tom Cat,   That   is Garfield.'
aList = re.split(r'\s+', aStr)
print ' '.join(reversed(aList))
