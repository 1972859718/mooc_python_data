# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 17:05:42 2018

@author: moon
"""

import requests
import re
def retrieve_dji_list():
    r = requests.get('http://money.cnn.com/data/dow30/')
    search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\n.*?class="wsod_stream">(.*?)<\/span>')
    dji_list_in_text = re.findall(search_pattern, r.text)
    return dji_list_in_text
dji_list = retrieve_dji_list()
for i in dji_list:
    print(i[0],':',i[1],'->',i[2])