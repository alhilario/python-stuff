#!/usr/bin/python
# -*- coding: utf-8 -*-

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    if (first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u'):
        new_word = word + pyg
    else:
        new_word = word[1:] + word[0] + pyg
    print new_word
else:
    print 'empty'
