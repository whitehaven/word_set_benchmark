#!/usr/bin/env python
import sys

total_words = 0
unique_words = 0
word_s = set()

for arg in sys.argv[1:]:
    with open(arg, 'r') as f:
        for line in f:
            total_words += 1
            word_s.add(line)

unique_words = len(word_s)

with open('output.txt', 'w') as out_f:
    print('total words:{}'.format(total_words))
    print('unique words: {}'.format(unique_words))
    print('word entries eliminated: {}'.format(total_words - unique_words))
    for w in sorted(word_s):
        out_f.write('{}'.format(w))

