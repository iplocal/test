# Converting between unicode and plain strings

ustr = u'Hello world'

utf8_str = ustr.encode('utf8')
ascii_str = ustr.encode('ascii')
iso_str = ustr.encode('iso8859-1')
utf16_str = ustr.encode('utf16')

print 'UTF8:', utf8_str
print 'ASCII:', ascii_str
print 'ISO:', iso_str
print 'UTF16:', utf16_str

pstr1 = unicode(utf8_str, 'utf8')
pstr2 = unicode(ascii_str, 'ascii')
pstr3 = unicode(iso_str, 'iso8859-1')
pstr4 = unicode(utf16_str, 'utf16')

for c in utf16_str:
    print hex(ord(c)),

print
print ' | '.join([pstr1, pstr2, pstr3, pstr4])
