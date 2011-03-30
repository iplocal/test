# Interpolating variables in a string

def expand(fmt, d, marker = '"', safe = False):
    def lookup(w):
        if safe:
            return d.get(w, w.join(marker * 2))
        else:
            return d[w]
    parts = fmt.split(marker)
    parts[1::2] = map(lookup, parts[1::2])
    return ''.join(parts)

if __name__ == '__main__':
    print expand('just "a" test', {'a': 'one'})
