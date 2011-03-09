# Accessing substrings

import lib
import struct

aField = lib.theStr[3:8]
print aField

fmt = '5s 3x 6s 6s'
numRemain = len(lib.theStr) - struct.calcsize(fmt)
aFmt = '%s %ds' % (fmt, numRemain)
l, s1, s2, t = struct.unpack(aFmt, lib.theStr)
print l, s1, s2, t

fivers = [lib.theStr[c:c+5] for c in xrange(0, len(lib.theStr), 5)]
print fivers

cuts = [4, 10, 16, 22]
pieces = [lib.theStr[i:j] for i, j in zip([0] + cuts, cuts + [None])]
print pieces
