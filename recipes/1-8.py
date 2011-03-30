# Checking whether a string contains a set of characters

def contain_any(seq, aset):
    for c in seq:
        if c in aset:
            return True

    return False

the_set = set(['a', 'b', 'c'])
print contain_any('cde', the_set)
print contain_any('def', the_set)

print bool(set('cde') & the_set)
print bool(set('def') & the_set)
