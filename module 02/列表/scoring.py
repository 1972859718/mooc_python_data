# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 16:51:17 2018

@author: moon
"""

#scoring.py
jScores = [9,9,8.5,10,7,8,8,9,8,10]
aScore = 9
jScores.sort()
jScores.pop()
jScores.pop(0)
jScores.append(aScore)
aveScore = sum(jScores) / len(jScores)
print(aveScore)