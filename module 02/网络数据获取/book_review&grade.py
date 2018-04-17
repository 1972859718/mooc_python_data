# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 15:39:52 2018

@author: moon
"""

import requests
from bs4 import BeautifulSoup
import re
sum = 0
i = 1
r = requests.get('https://book.douban.com/subject/1084336/')
soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('p', 'comment-content')
for item in pattern:
    print('评论',i,':',item.string)
    i +=1
pattern_s = re.compile('<span class="user-stars allstar(.*?)rating"')
p = re.findall(pattern_s, r.text)
for star in p:
    sum += int(star)
print("这本书的评分是：",sum)