# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:57:01 2019

@author: JUFRI
"""
import re
def abbreviation(kata):
    
    i=0
    for i in range(len(kata)):
        a=re.findall("[A-Z]",kata[i])
        if a:
            print(a)

abbreviation(input("kata apa yang ingin disingkat? "))