# Trimming space from the ends of a string

astr = '     abc   '

print '|', astr.lstrip(), '|', astr.rstrip(), '|', astr.strip(), '|'

astr = 'xyzzydxabc yzxzxy'

print '|' + astr.strip('xyz') + '|'
