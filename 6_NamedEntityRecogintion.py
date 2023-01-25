from nltk.chunk import ne_chunk
from nltk.tag import pos_tag

words = ['Mr.', 'Smith', "'s", 'train', 'leave', '12']

tagged = pos_tag(words)

ner = ne_chunk(tagged)
ner.draw()