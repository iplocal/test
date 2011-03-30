# Test whether an object is string-like

def is_str(obj):
    return isinstance(obj, basestring)

print is_str('abc')
print is_str(123)
