from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

eng_stopwords = stopwords.words('english')

sentence = "Mr. Smith's train does not leave at 12 AM."
list_word = word_tokenize(sentence)

# Remove Stop Words
# List Comprehension
removed_stopwords_list = [word for word in list_word if word.lower() not in eng_stopwords]

# Same as this
# for word in list_word:
#     if word not in eng_stopwords:
#         removed_stopwords_list.append(word)

print('Removed Stopwords: ', end='')
print(removed_stopwords_list)

#Remove Punctuation
import string

removed_punctuation_list = [word for word in removed_stopwords_list if word not in string.punctuation]

print('Removed Punctiations: ', end='')
print(removed_punctuation_list)
