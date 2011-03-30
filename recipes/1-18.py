# Replacing multiple patterns in a single pass

import re

def multi_replace(text, adict):
    pattern = re.compile('|'.join(map(re.escape, adict)))
    def trans(match):
        return adict[match.group(0)]
    return pattern.sub(trans, text)

print multi_replace('this is thing', {'thing': 'something'})
