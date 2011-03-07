# Accessing substrings

import com
import struct

aField = com.theStr[3:8]
print aField

fmt = '5s 3x 6s 6s'
numRemain = len(com.theStr) - struct.calcsize(fmt)
aFmt = '%s %ds' % (fmt, numRemain)
l, s1, s2, t = struct.unpack(aFmt, com.theStr)
print l, s1, s2, t

fivers = [com.theStr[c:c+5] for c in xrange(0, len(com.theStr), 5)]
print fivers

cuts = [4, 10, 16, 22]
pieces = [com.theStr[i:j] for i, j in zip([0] + cuts, cuts + [None])]
print pieces
