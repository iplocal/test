# Trimming space from the ends of a string

aStr = '     abc   '

print '|', aStr.lstrip(), '|', aStr.rstrip(), '|', aStr.strip(), '|'

aStr = 'xyzzydxabc yzxzxy'

print '|' + aStr.strip('xyz') + '|'
