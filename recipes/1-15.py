# Expanding and compressing tabs

import lib
import re

def unexpand(aStr, tabLen = 8):
    pieces = re.split(r'( +)', aStr.expandtabs(tabLen))
    curLen = 0
    for i, piece in enumerate(pieces):
        thisLen = len(piece)
        curLen += thisLen
        if piece.isspace():
            nTabs = curLen / tabLen - (curLen - thisLen) / tabLen
            if nTabs > 0:
                nBlanks = curLen % tabLen
                pieces[i] = '\t' * nTabs + ' ' * nBlanks
            # nBlanks = curLen % tabLen
            # nTabs = (thisLen - nBlanks + tabLen - 1) / tabLen
            # pieces[i] = '\t' * nTabs + ' ' * nBlanks
    return ''.join(pieces)

# tabLen = 8
# print ('|'.ljust(tabLen)) * 10
print unexpand('this        is a string')
