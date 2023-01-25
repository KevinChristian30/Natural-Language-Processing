from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.classify import NaiveBayesClassifier, accuracy
import string
import random
import pickle

positive = open('positive.txt', 'r').read()
negative = open('negative.txt', 'r').read()

# Data Preprocessing
list_words = word_tokenize(positive) + word_tokenize(negative)

eng_stopwords = stopwords.words('english')
list_words = [word for word in list_words if word.lower() not in eng_stopwords]
list_words = [word for word in list_words if word not in string.punctuation]
list_words = [word for word in list_words if word.isalpha()]

freqDist = FreqDist(list_words)
list_words = [word for word in freqDist.most_common(100)]

# Labeling Sentence
labeled_sentence = []
for sentence in positive.split('\n'):
  labeled_sentence.append((sentence, 'pos'))

for sentence in negative.split('\n'):
  labeled_sentence.append((sentence, 'neg'))

# Make Data Set
dataset = []
for sentence, label in labeled_sentence:
  dict = {}
  words = word_tokenize(sentence)

  for feature in list_words:
    dict[feature] = feature in words

  dataset.append((dict, label))

random.shuffle(dataset)

counter = int(len(dataset) * 0.7)
training_data = dataset[:counter]
testing_data = dataset[counter:]

classifier = NaiveBayesClassifier.train(training_data)
# print(accuracy(classifier, testing_data) * 100, '%')

# Make The Model
file = open('model.pickle', 'wb')
pickle.dump(classifier, file)
file.close()

