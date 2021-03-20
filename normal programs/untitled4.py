# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 17:36:16 2019

@author: DELL
"""
"""wap to find subsets and operations on them"""
import itertools
p=[]
m=1
a=list(map(int,input().split()))
for k in range(2,len(a)+1):
    for i in itertools.combinations(a,k):
        q=list(i)
        print(q)
        for j in q:
            m=m*j
        p.append(m//sum(q))
        m=1
print(p)
print(max(p))
