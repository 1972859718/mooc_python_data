# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 17:05:32 2018

@author: moon
"""

def clean_list(lst):
    cleaned_list = []
    for item in lst:
        for c in item:
            if c.isalpha() != True:
                 item = item.replace(c, '')
        cleaned_list.append(item)
    return cleaned_list                                            
 
if __name__ == "__main__":
    coffee_list = ['32Latte', '_Americano30', '/34Cappuccino', 'Mocha35']
    cleaned_list = clean_list(coffee_list)
    for k,v in zip(range(1, len(cleaned_list)+1), cleaned_list):
        print(k, v)