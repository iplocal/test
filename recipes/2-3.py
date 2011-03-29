# Searching and replacing text in a file

import os, sys

num_args = len(sys.argv)

if not 3 <= num_args <= 5:
    print 'Usage: %s search-text replace-text [infile [outfile]]' % \
        os.path.basename(sys.argv[0])
else:
    stext = sys.argv[1]
    rtext = sys.argv[2]
    ifile = sys.stdin
    ofile = sys.stdout
    if num_args > 3:
        ifile = open(sys.argv[3])
    if num_args > 4:
        ofile = open(sys.argv[4], 'w')
    for strings in ifile:
        ofile.write(strings.replace(stext, rtext))
    ifile.close()
    ofile.close()
