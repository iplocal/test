# Replacing multiple patterns in a single pass

import re

def multiReplace(text, aDict):
    pattern = re.compile('|'.join(map(re.escape, aDict)))
    def trans(match):
        return aDict[match.group(0)]
    return pattern.sub(trans, text)

print multiReplace('this is thing', {'thing': 'something'})
