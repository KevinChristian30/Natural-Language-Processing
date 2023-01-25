from nltk.tag import pos_tag

words = ['Mr.', 'Smith', "'s", 'train', 'leave', '12']

tagged = pos_tag(words)
print(tagged)

# Tag Explanation
# https://pythonprogramming.net/natural-language-toolkit-nltk-part-speech-tagging/
