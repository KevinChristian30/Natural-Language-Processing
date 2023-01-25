from nltk.corpus import gutenberg

print(gutenberg.fileids())
print(gutenberg.raw('shakespeare-hamlet.txt'))

# Corpora From Web

from urllib import request
url = 'https://www.gutenberg.org/files/63919/63919.txt'

corpus = request.urlopen(url).read().decode('utf-8')

