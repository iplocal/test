# Expanding and compressing tabs

import re

def unexpand(astr, tab_len = 8):
    pieces = re.split(r'( +)', astr.expandtabs(tab_len))
    cur_len = 0
    for i, piece in enumerate(pieces):
        this_len = len(piece)
        cur_len += this_len
        if piece.isspace():
            ntab = cur_len / tab_len - (cur_len - this_len) / tab_len
            if ntab > 0:
                nblank = cur_len % tab_len
                pieces[i] = '\t' * ntab + ' ' * nblank
    return ''.join(pieces)

# tab_size = 8
# print ('|'.ljust(tab_size)) * 10
print unexpand('this        is a string')
