from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.classify import NaiveBayesClassifier, accuracy
from nltk.stem import PorterStemmer
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.corpus import wordnet
from urllib import request
import string
import random
import pickle
import csv

class Utility:
  def clear():
    for i in range(30): print()

tagged = ''
ner = ''

class NaiveBayes:

  def getModel():

    Utility.clear()
    print('Creating Model...')

    with open('C:\\Users\\Kevin\\Desktop\\Answer\\negative.csv', newline='') as csvfile:
      negCSV = list(csv.reader(csvfile))

    with open('C:\\Users\\Kevin\\Desktop\\Answer\\positive.csv', newline='') as csvfile:
      posCSV = list(csv.reader(csvfile))

    eng_stopwords = stopwords.words('english')

    positive, negative = '', ''

    for i in posCSV: 
      positive += str(i[0])
    for i in negCSV: 
      negative += str(i[0])

    list_words = word_tokenize(positive) + word_tokenize(negative)

    list_words = [word for word in list_words if word.lower() not in eng_stopwords]
    list_words = [word for word in list_words if word not in string.punctuation]
    list_words = [word for word in list_words if word.isalpha()]

    global tagged, ner 
    tagged = pos_tag(list_words)
    ner = ne_chunk(tagged)

    porter_stemmer = PorterStemmer()
    list_words = [porter_stemmer.stem(word) for word in list_words]

    freqDist = FreqDist(list_words)
    list_words = [word for word in freqDist.most_common(1000)] # Tinggal ganti

    labeled_sentence = []
    for sentence in positive.split('\n'):
      labeled_sentence.append((sentence, 'Positive'))

    for sentence in negative.split('\n'):
      labeled_sentence.append((sentence, 'Negative'))      

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

    print('Model Created with an accuracy of: ')
    print(accuracy(classifier, testing_data) * 100, '%')
    print('Press Enter to Continue')
    input()

    return classifier

  def loadModel(name):
    file = open(name + '.pickle', 'rb')
    model = pickle.load(file)
    file.close()
    return model

class Corpora:
  def loadCorpus():
    Utility.clear()

    url = 'https://www.gutenberg.org/files/63919/63919.txt'
    corpus = request.urlopen(url).read().decode('utf-8')

    words = corpus.split()

    i = 0
    for word in words:
      i += 1
      synsets = wordnet.synsets(word)
      for synset in synsets:
        print(f"{synset}: {synset.definition()}")
        for lemma in synset.lemmas():
          print(f"Synonim: {lemma.name()}")
          for antonym in lemma.antonyms():
            print(f"Antonym: {antonym.name()}")
        print()
      if i >= 100: break

class Classification:
  Utility.clear()

  def loop():
    model = NaiveBayes.getModel()

    while (True):
      print('0. Exit')
      print('1. Save Model')
      print('2. View Model POS Tag')
      print('3. View Model NER')
      review = input('Input Review (0 to Exit):  ')

      if (review == '0'): break
      if (review == '1'): 
        name = input('Enter Model Name: ')
        file = open(name + '.pickle', 'wb')
        pickle.dump(model, file)
        file.close()
        print('Model Saved...')
        continue
      if (review == '2'):
        print(tagged)
        continue
      if (review == '3'):
        print(ner)
        continue
      
      # Musn't contain #
      if (review.__contains__('#')):
        continue

      result = model.classify(FreqDist(review))

      print('Result: ' + result)
      print()

class ExitView:
  def quit():
    print('Bye :)')
    input()
    exit(0)

class MainMenu:
  def displayCommands():
    Utility.clear()
    print('Natural Langguage Processing')
    print('1. Women Clothes Review Classification')
    print('2. Load Corpus')
    print('0. Exit')

  def route(command):
    if (command == '0'): 
      ExitView.quit()
    elif (command == '1'): 
      Classification.loop()
    elif (command == '2'):
      Corpora.loadCorpus()
    else :
      print('Invalid Input')
      input('Press Enter')

  def loop():
    while (True):
      MainMenu.displayCommands()
      command = input('>> ')
      MainMenu.route(command)


def main():
  MainMenu.loop()

main()