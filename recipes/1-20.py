# Handling international text with unicode

germanAe = unicode('\xc3\xa4', 'utf8')

sentence1 = 'This is a ' + germanAe
sentence2 = 'Easy!'
para = '. '.join([sentence1, sentence2])

print para
