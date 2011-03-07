# Test whether an object is string-like

def isStr(obj):
    return isinstance(obj, basestring)

print isStr('abc')
print isStr(123)
