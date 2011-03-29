# Reading from a file

file_obj = open('../README')

try:
    all_lines = file_obj.readlines()
finally:
    file_obj.close()

for line in all_lines:
    print line.rstrip('\n')
