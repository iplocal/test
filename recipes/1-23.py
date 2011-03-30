# Encoding unicode data for xml and html

import codecs
from htmlentitydefs import codepoint2name

def enc_for_xml(uni_data, encoding = 'ascii'):
    return uni_data.encode(encoding, 'xmlcharrefreplace')

def html_replace(exc):
    if isinstance(exc, (UnicodeEncodeError, UnicodeTranslateError)):
        s = [u'&%s;' % codepoint2name[ord(c)]
             for c in exc.object[exc.start:exc.end]]
        return ''.join(s), exc.end
    else:
        raise TypeError("can't handle %s" % exc.__name__)

codecs.register_error('html_replace', html_replace)

def enc_for_html(uni_data, encoding = 'ascii'):
    return uni_data.encode(encoding, 'html_replace')

if __name__ == '__main__':
    data = u"""\
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
"""
    print enc_for_xml(data)
    print enc_for_xml(data, 'utf8')
