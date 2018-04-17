# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 22:29:00 2018

@author: moon
"""

def countchar(str):
    list = []
    for i in range(65,65+26):
        list.append(str.count(chr(i))+str.count(chr(i+32)))
    return list
if __name__ == "__main__":
    str = input()
    print(countchar(str))