# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 16:32:55 2018

@author: moon
"""

#compare.py,判断是否为回文数
sStr = "acdhdca"
if(sStr == ''.join(reversed(sStr))):
    print("Yes")
else:
    print('No')