# Checking a string for any of multiple endings

def any_ends(pred, seq):
    #return True in itertools.imap(pred, seq)
    return True in map(pred, seq)

def ends_with(s, *endings):
    return any_ends(s.endswith, endings)

files = ['abc.jpg', 'def.txt', 'ghi.gif']

for file_name in files:
    if ends_with(file_name, '.jpg', '.gif'):
        print file_name

