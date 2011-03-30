# Simplifying usage of strings' translate method

import string

def translator(frm = '', to = '', delete = '', keep = None):
    if len(to) == 1:
        to = to * len(frm)
    trans = string.maketrans(frm, to)
    if keep != None:
        all_chars = string.maketrans('', '')
        delete = all_chars.translate(all_chars, keep.translate(all_chars, delete))
    def translate(s):
        return s.translate(trans, delete)
    return translate

astr = 'Chris Perkins: 224-7992'
digit_only = translator(keep = string.digits)
print digit_only(astr)

no_digit = translator(delete = string.digits)
print no_digit(astr)

digit_to_hash = translator(frm = string.digits, to = '#')
print digit_to_hash(astr)
