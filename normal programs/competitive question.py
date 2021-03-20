# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:02:30 2020

@author: DELL
"""
for de in range(int(input("please enter a range"))):
    l=[]
    qw=list(map(int,input("please enter number seperated by space").split()))
    n=qw[0] 
    trace=qw[1]
    m=trace/n
    if(m in range(1,n+1)):
        print("Case #{}: POSSIBLE".format(de+1))
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
            for i in range(len(l)):
                for j in range(len(l[0])):
                    if(l[i][j]==v):
                        print(1,end=" ")
                    elif(l[i][j]==1):
                        print(v,end=" ")
                    else:    
                        print(l[i][j],end=' ')
                print()
        printLatin(n,int(m))       
    else:
        print("Case #{}: IMPOSSIBLE".format(de+1))
print("---------------------------------------------------")