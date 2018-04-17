# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:17:03 2018

@author: moon
"""

import requests, re, time
from bs4 import BeautifulSoup
count = 0
i = 0
sum, count_s = 0, 0
while(count < 50):
    try:
        r = requests.get('https://book.douban.com/subject/bookid/1084336/hot?p=' + str(i+1))
    except Exception as err:
        print(err)
        break
    soup = BeautifulSoup(r.text, 'lxml')
    comments = soup.find_all('p', 'comment-content')
    for item in comments:
        count = count + 1
        print(count, item.string)
        if count == 50:
            break
    pattern = re.compile('<span class="user-stars allstar(.*?) rating"')
    p = re.findall(pattern, r.text)
    for star in p:
        count_s = count_s + 1
        sum += int(star)
    time.sleep(5) # delay request from douban's robots.txt
    i += 1
if count == 50:
    print(sum / count_s)