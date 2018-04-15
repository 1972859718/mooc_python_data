# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 16:15:07 2018

@author: moon
"""

#filename:tonumf_3_4.py
astr='My moral standing  is: 0.98765'
tempstr1=astr.split(':')[1]
tempstr2=tempstr1.split(' ')[1]
print(float(eval(tempstr2)))