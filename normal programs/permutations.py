# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 17:26:38 2020

@author: DELL
"""
from itertools import permutations
m = []
a=0
l =0
perm = list(map(list,set(permutations([1,2,1]))))
for i in range(len(perm)):
    for j in range(3):
        a+=perm[i][j]*(10**j)
        if(a>=l):
            l=a
    a=0
print(l)
print(len(perm))