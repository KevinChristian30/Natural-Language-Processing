import pickle
from nltk.classify import accuracy
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

file = open('model.pickle', 'rb')
classifier = pickle.load(file)
file.close()

review = input("Input Review: ")
words = word_tokenize(review)
result = classifier.classify(FreqDist(review))

print(result)
