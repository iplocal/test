# Filtering a string for a set of characters

import string

allChars = string.maketrans('', '')

def makeFilter(keep):
    delChars = allChars.translate(allChars, keep)
    def theFilter(s):
        return s.translate(allChars, delChars)
    return theFilter

if __name__ == '__main__':
    justVowels = makeFilter('aeiouy')
    print justVowels('four score and seven years ago')
    print justVowels('tiger, tiger burning bright')
