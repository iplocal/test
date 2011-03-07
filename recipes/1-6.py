# Combining strings

import operator

s1 = 'Tom'
s2 = 'Garfield'

s = 'Two cats: %s and %s' % (s1, s2)

print s

s = 'Again the cats: {0} and {1}'.format(s1, s2)

print s

cats = [s1, s2]
print reduce(operator.add, cats)
