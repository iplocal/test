# Interpolating variables in a string

def expand(fmt, d, marker = '"', safe = False):
    if safe:
        def lookup(w):
            return d.get(w, w.join(marker * 2))
    else:
        def lookup(w):
            return d[w]
    parts = fmt.split(marker)
    parts[1::2] = map(lookup, parts[1::2])
    return ''.join(parts)

if __name__ == '__main__':
    print expand('just "a" test', {'a': 'one'})
