# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:29:29 2020

@author: DELL
"""
count=1
l=[]
for i in  range(7,99,2):
    if(i%3==0 or i%5==0 ):
        pass
    else:
        l.append(i)
k=[]
for j in l:
    if((j+6) in l):
        z=j+6
        k.append((j+6,j))
print(k)