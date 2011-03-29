# Counting lines in a file

file_obj = open('../README', 'rU')
count = len(file_obj.readlines())
file_obj.close()

print count
