# Reversing a string by words or characters

import lib
import re

print lib.the_str[::-1]

alist = lib.the_str.split()
alist.reverse()
print alist

astr = 'This is  Tom Cat,   That   is Garfield.'
alist = re.split(r'\s+', astr)
print ' '.join(reversed(alist))
