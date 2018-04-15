# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
r = requests.get('https://book.douban.com/subject/1084336/')
soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('p', 'comment-content')
for item in pattern:
    print(item.string)
