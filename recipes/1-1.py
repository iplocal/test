# Processing a string one character at a time

import lib

alist = list(lib.the_str)
print alist

for c in lib.the_str:
    print c,

print
print '\''.join(c for c in lib.the_str)
