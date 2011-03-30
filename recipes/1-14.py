# Changing the indentation of a multiline string

def re_indent(astr, nspace):
    spaces = nspace * ' '
    lines = [spaces + line.strip() for line in astr.splitlines()]
    return '\n'.join(lines)

s = """\
   line one
     line two
 and line three\
"""

print 'before indent'.center(30, '-')
print s
print 'after indent'.center(30, '-')
print re_indent(s, 4)
