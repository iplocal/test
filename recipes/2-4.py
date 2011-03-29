# Reading a specific line from a file

import linecache

file_path = '../README'
the_line = linecache.getline(file_path, 2)
print the_line.rstrip('\n')
