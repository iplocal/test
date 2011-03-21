# Encoding unicode data for xml and html

import codecs
from htmlentitydefs import codepoint2name

def encForXml(uniData, encoding = 'ascii'):
    return uniData.encode(encoding, 'xmlcharrefreplace')

def htmlReplace(exc):
    if isinstance(exc, (UnicodeEncodeError, UnicodeTranslateError)):
        s = [u'&%s;' % codepoint2name[ord(c)]
             for c in exc.object[exc.start:exc.end]]
        return ''.join(s), exc.end
    else:
        raise TypeError("can't handle %s" % exc.__name__)

codecs.register_error('htmlReplace', htmlReplace)

def encForHtml(uniData, encoding = 'ascii'):
    return uniData.encode(encoding, 'htmlReplace')

if __name__ == '__main__':
    data = u'''\
<html>
<head>
<title>Encoding Test</title>
</head>
<body>
<p>accented characters:
<ul>
<li>\xe0 (a + grave)
<li>\xe7 (c + cedilla)
<li>\xe9 (e + acute)
</ul>
<p>symbols:
<ul>
<li>\xa3 (British pound)
<li>\u20ac (Euro)
<li>\u221e (infinity)
</ul>
</body>
</html>
'''
    print encForXml(data)
    print encForHtml(data, 'utf8')
