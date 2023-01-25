from nltk.stem import WordNetLemmatizer

words = ['writes', 'write', 'written', 'writing', 'program', 'programmer', 'programming']

wnl = WordNetLemmatizer()
word = 'good'

adverb = wnl.lemmatize(word, pos='a') # a = Adverb
verb = wnl.lemmatize(word, pos='v') # v = Verb
adjective = wnl.lemmatize(word, pos='r') # r = Adjective
noun = wnl.lemmatize(word, pos='n') # n = noun

print('Original Word: ' + word)
print('Adverb: ' + adverb)
print('Verb: ' + verb)
print('Adjective: ' + adjective)
print('Noun: ' + noun)
