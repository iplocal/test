# Accessing substrings

import lib
import struct

afield = lib.the_str[3:8]
print afield

fmt = '5s 3x 6s 6s'
num_remain = len(lib.the_str) - struct.calcsize(fmt)
afmt = '%s %ds' % (fmt, num_remain)
l, s1, s2, t = struct.unpack(afmt, lib.the_str)
print l, s1, s2, t

fivers = [lib.the_str[c:c+5] for c in xrange(0, len(lib.the_str), 5)]
print fivers

cuts = [4, 10, 16, 22]
pieces = [lib.the_str[i:j] for i, j in zip([0] + cuts, cuts + [None])]
print pieces
