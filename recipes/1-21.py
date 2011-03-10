# Converting between unicode and plain strings

uStr = u'Hello world'

utf8Str = uStr.encode('utf8')
asciiStr = uStr.encode('ascii')
isoStr = uStr.encode('iso8859-1')
utf16Str = uStr.encode('utf16')

print 'UTF8:', utf8Str
print 'ASCII:', asciiStr
print 'ISO:', isoStr
print 'UTF16:', utf16Str

pStr1 = unicode(utf8Str, 'utf8')
pStr2 = unicode(asciiStr, 'ascii')
pStr3 = unicode(isoStr, 'iso8859-1')
pStr4 = unicode(utf16Str, 'utf16')

for c in utf16Str:
    print hex(ord(c)),

print
print ' | '.join([pStr1, pStr2, pStr3, pStr4])
