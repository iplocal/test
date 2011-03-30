# Filtering a string for a set of characters

import string

all_chars = string.maketrans('', '')

def make_filter(keep):
    del_chars = all_chars.translate(all_chars, keep)
    def the_filter(s):
        return s.translate(all_chars, del_chars)
    return the_filter

if __name__ == '__main__':
    just_vowels = make_filter('aeiouy')
    print just_vowels('four score and seven years ago')
    print just_vowels('tiger, tiger burning bright')
