#!/usr/bin/env python
"""reducer.py"""

import sys
from operator import itemgetter

current_word = None
current_count = 0
word = None
keys = [0]
words = {0:''}

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except:
        continue
    if current_word == word:
        current_count +=count
    else:
        if current_word:
            if current_count > keys[0]:
                if len(keys) == 10:
                    d = words.pop(keys[0])
                    d = keys.pop(0)
                words[current_count] = current_word
                keys.append(current_count)
                keys.sort()
            # print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

if current_word == word:
    if current_count > keys[0]:
        if len(keys) == 10:
            d = words.pop(keys[0])
            d = keys.pop(0)
        words[current_count] = current_word
        keys.append(current_count)
    # print('%s\t%s' % (current_word, current_count))

if keys[0] == 0 and len(keys) > 1:
    d = words.pop(keys[0])

for key, word in words.items():
    print('%s\t%s' % (word, key))



