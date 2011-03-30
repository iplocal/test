# Making some strings case-insensitive

class istr(str):
    """Case insensitive string class.

    Behaves just like str, except that all comparisions and lookups
    are case insensitive.
    """
    def __init__(self, ostr):
        str.__init__(self)
        self._lowered = ostr.lower()
    def __repr__(self):
        return '%s(%s)' % (type(self).__name__, str.__repr__(self))
    def __hash__(self):
        return hash(self._lowered)
    def lower(self):
        return self._lowered

def _make_case_ins(name):
    """wrap one method of str into an istr one, case-insensitive"""
    str_method = getattr(str, name)
    def x(self, other, *args):
        """The case-insensitive method substitution.

        Try lowercasing "other", which is typically a string, but
        be prepared to use it as-is if lowering gives problems, since
        strings CAN be correctly compared with non-strings.
        """
        try: other = other.lower()
        except (TypeError, AttributeError, ValueError): pass
        return str_method(self._lowered, other, *args)
    setattr(istr, name, x)

for name in 'eq lt le gt ge ne contains'.split():
    _make_case_ins('__%s__' % name)

for name in 'count endswith find index rfind rindex startswith'.split():
    _make_case_ins(name)

del _make_case_ins

tstr = istr('AAAbbb')
print vars(tstr)
print istr('Abc Def').find('DEF')

