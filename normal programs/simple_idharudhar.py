# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:02:30 2020

@author: DELL
"""
def printLatin(n,v):   
        k = n + 1
        l=[]
        for i in range(1, n + 1, 1):  
            g=[]      
            temp = k  
            while (temp <= n) : 
                g.append(temp)
                temp += 1
            for j in range(1, k): 
                g.append(j)
            k -= 1
            l.append(g)
        print(l)
        for i in range(len(l)):
            for j in range(len(l[0])):
                if(l[i][j]==v):
                    print(1,end=" ")
                elif(l[i][j]==1):
                    print(v,end=" ")
                else:    
                    print(l[i][j],end=' ')
            print()
printLatin(1,1)