# Making some strings case-insensitive

class iStr(str):
    '''Case insensitive string class.

    Behaves just like str, except that all comparisions and lookups
    are case insensitive.
    '''
    def __init__(self, *args):
        self._lowered = str.lower(self)
    def __repr__(self):
        return '%s(%s)' % (type(self).__name__, str.__repr__(self))
    def __hash__(self):
        return hash(self._lowered)
    def lower(self):
        return self._lowered

def _makeCaseIns(name):
    '''wrap one method of str into an iStr one, case-insensitive'''
    strMethod = getattr(str, name)
    def x(self, other, *args):
        '''
        Try lowercasing "other", which is typically a string, but
        be prepared to use it as-is if lowering gives problems, since
        strings CAN be correctly compared with non-strings.
        '''
        try: other = other.lower()
        except (TypeError, AttributeError, ValueError): pass
        return strMethod(self._lowered, other, *args)
    setattr(iStr, name, x)

for name in 'eq lt le gt ge ne str contains'.split():
    _makeCaseIns('__%s__' % name)

for name in 'count endswith find index rfind rindex startswith'.split():
    _makeCaseIns(name)

del _makeCaseIns

print iStr('Abc Def').find('DEF')

