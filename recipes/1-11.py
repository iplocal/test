# Checking whether a string is text or binary
# -*- coding: utf-8 -*-

from __future__ import division
import string

textChars = ''.join(map(chr, range(32, 127))) + '\n\r\t\b'
allChars = string.maketrans('', '')

def isText(s, txt = textChars, threshold = 0.30):
    if '\0' in s:
        return False
    if not s:
        return True
    t = s.translate(allChars, txt)
    return (len(t) / len(s) <= threshold)

print isText('this is a text string')
print isText('àÃ¨Ã©Ã¬Ã2Ã1')
