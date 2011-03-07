# Simplifying usage of strings' translate method

import string

def translator(frm = '', to = '', delete = '', keep = None):
    if len(to) == 1:
        to = to * len(frm)
    trans = string.maketrans(frm, to)
    if keep != None:
        allChars = string.maketrans('', '')
        delete = allChars.translate(allChars, keep.translate(allChars, delete))
    def translate(s):
        return s.translate(trans, delete)
    return translate

aStr = 'Chris Perkins: 224-7992'
digitOnly = translator(keep = string.digits)
print digitOnly(aStr)

noDigit = translator(delete = string.digits)
print noDigit(aStr)

digitToHash = translator(frm = string.digits, to = '#')
print digitToHash(aStr)
