from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

sentence = 'I order a bowl of chicken rice and a bowl of ramen, but I hate the chicken'

fd = FreqDist(word_tokenize(sentence))

for word, count in fd.most_common():
  print(f"{word}: {count}")
