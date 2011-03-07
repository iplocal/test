# Checking whether a string contains a set of characters

def containAny(seq, theSet):
    for c in seq:
        if c in theSet:
            return True

    return False

theSet = set(['a', 'b', 'c'])
print containAny('cde', theSet)
print containAny('def', theSet)

print bool(set('cde') & theSet)
print bool(set('def') & theSet)
