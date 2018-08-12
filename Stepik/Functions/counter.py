#! /usr/bin/env python3
from collections import Counter
for word, amount in Counter(input().lower().split()).most_common():
    print(word, amount)