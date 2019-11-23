# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 11:28:44 2019

@author: JUFRI
"""
import re
def arkademy(k):
    a=re.findall("[a-zA-Z]", k)
    if a:
        print("Ini Bukan Angka!")
    else:
        x=int(k)
        print (x)
        i=1
        while i<=x:
            if i%3!=0 and i%7!=0:
                print (i)
            elif i%3==0 and i%7==0:
                print("Arkademy")
            elif i%3==0:
                print("Arka")
            elif i%7==0:
                print("Demy")
            i += 1
        
arkademy(input("Masukan Angaka disini: "))