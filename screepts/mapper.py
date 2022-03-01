#!/usr/bin/env python
"""mapper.py"""

import sys
import re

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        word = re.sub("[^A-Za-z]", "", word)
        word = word.lower()
        if word:
            print('%s\t%s' % (word, 1))

