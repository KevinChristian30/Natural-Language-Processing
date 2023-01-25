from nltk.tokenize import word_tokenize, sent_tokenize

sentence = "Mr. Smith's train does not leave at 12 AM."
list_word = word_tokenize(sentence)

paragraph = "Mr. Smith's train does not leave at 12 AM. They speak English at work. I have no money at the moment"
list_sentence = sent_tokenize(paragraph)

print(list_word)
print(list_sentence)