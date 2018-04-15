# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 16:17:05 2018

@author: moon
"""

#filename:num_3_4.py
astr='I like Python very much 2333 because Python is very cute 666.'
count=0
for c in astr:
    if c<'A' and c>='0':
        count+=1
print(count)#输出字母个数
newstr = ''
for s in astr:
    if s.isalpha():
        newstr += s
    if s.isspace():
        newstr += s
print(newstr)
bstr=newstr.split(' ')
print(bstr)
for i in bstr:
   if '' in bstr:
        bstr.remove('')#去掉列表中的空格
print(bstr)
print(len(bstr))#输出单词个数
cstr=astr.replace('Python','Gao Lin',1)#将第一个Python替换成Gao Lin
print(cstr)