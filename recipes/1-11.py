# Checking whether a string is text or binary
# -*- coding: utf-8 -*-

from __future__ import division
import string

text_chars = ''.join(map(chr, range(32, 127))) + '\n\r\t\b'
all_chars = string.maketrans('', '')

def is_text(s, txt = text_chars, threshold = 0.30):
    if '\0' in s:
        return False
    if not s:
        return True
    t = s.translate(all_chars, txt)
    return (len(t) / len(s) <= threshold)

print is_text('this is a text string')
print is_text('àÃ¨Ã©Ã¬Ã2Ã1')
