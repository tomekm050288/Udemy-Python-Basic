# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 18:35:57 2020

@author: tm
"""


data = ['Error:File cannot be open','Error:No free space on disk',
        'Error:File missing','Warning:Internet connection lost',
        'Error:Access denied']

for item in data:
    print(item.upper())
    
    
for item in data:
    elements = item.split(":")
    print(elements[0], elements[1])
    
   
    
for item in data:
    elements = item.split(":")
    if "Error" in elements[0]:
        print(elements[1].upper())
    else:
        print(elements[1])