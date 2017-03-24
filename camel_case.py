#!/bin/python

import sys
import string

s = raw_input().strip()
uppercase_chars = 0
for c in s:
    if c.upper() == c:
        uppercase_chars += 1 
print(uppercase_chars + 1)