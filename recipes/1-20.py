# Handling international text with unicode

german_ae = unicode('\xc3\xa4', 'utf8')

sentence1 = 'This is a ' + german_ae
sentence2 = 'Easy!'
para = '. '.join([sentence1, sentence2])

print para
