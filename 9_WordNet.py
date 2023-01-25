from nltk.corpus import wordnet

word = 'good'
synsets = wordnet.synsets(word)

for synset in synsets:
  print(f"{synset}: {synset.definition()}")
  for lemma in synset.lemmas():
    print(f"Synonim: {lemma.name()}")
    for antonym in lemma.antonyms():
      print(f"Antonym: {antonym.name()}")
  print()