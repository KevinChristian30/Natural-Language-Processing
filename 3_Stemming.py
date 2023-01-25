from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer

porter_stemmer = PorterStemmer()
snowball_stemmer = SnowballStemmer('english')
lancaster_stemmer = LancasterStemmer()

words = ['writes', 'write', 'written', 'writing', 'program', 'programmer', 'programming']

for word in words:
    print(f"PorterStemer: {porter_stemmer.stem(word)}")
    print(f"SnowballStemmer: {snowball_stemmer.stem(word)}")
    print(f"LancasterStemmer: {lancaster_stemmer.stem(word)}")
    print('-----------')
