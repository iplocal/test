# Writing to a file

file_obj = open('file.txt', 'w')

all_text = """\
This is a plain text file.
Used for test only.

Do not add to source repository.
"""

file_obj.write(all_text)
file_obj.close()
