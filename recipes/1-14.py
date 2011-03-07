# Changing the indentation of a multiline string

def reIndent(s, nSpaces):
    spaces = nSpaces * ' '
    lines = [spaces + line.strip() for line in s.splitlines()]
    return '\n'.join(lines)

s = '''\
   line one
     line two
 and line three\
'''

print 'before indent'.center(30, '-')
print s
print 'after indent'.center(30, '-')
print reIndent(s, 4)
