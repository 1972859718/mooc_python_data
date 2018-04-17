# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:42:17 2018

@author: moon
"""

import requests
re = requests.get('http://money.cnn.com/data/dow30/')
print(re.text)