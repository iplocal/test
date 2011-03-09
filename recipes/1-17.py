# Interpolating variables in a string in Python 2.4

import string

tmpl = string.Template('this is $thing')
print tmpl.substitute({'thing': 5})
print tmpl.substitute({'thing': 'test'})

print tmpl.substitute(thing = 'something')
