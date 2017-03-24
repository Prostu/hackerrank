#!/bin/python

import sys
import string
from pprint import pprint

h = map(int, raw_input().strip().split(' '))
word = raw_input().strip()
max_h = max([h[string.lowercase.index(u)] for u in word])
print(max_h * len(word))