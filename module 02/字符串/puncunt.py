# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 16:24:52 2018

@author: moon
"""

#puncunt.py
aStr = "Hello, World!"
bStr = aStr[:7] + "Python!"
count = 0
for ch in bStr[:]:
    if ch in ',.!?':
        count += 1
print(count)