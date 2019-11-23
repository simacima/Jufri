# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 19:33:37 2019

@author: JUFRI
"""

def pairSocks(cocok):
    print (cocok)
    i=0
    a=0
    for i in range (len(cocok)):
        for k in range (i+1, len(cocok)):
            if cocok[i]==cocok[k]:
                a=a+1
    print (a)
        
dicocok = [1,5,1,7,8,6,8,9,4,5]
pairSocks(dicocok)
