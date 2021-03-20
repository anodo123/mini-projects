# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 13:24:14 2018

@author: DELL
"""
rm=int(input("enter the number of rooms: "))
kr = list(map(input("enter the charges: ").split()))
rvn = int(input("enter the revenue: "))
a={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
i=1
m=[]
while(i<=12):
    for j in range(1,a[i]+1):
        #formula=(6-M)^2 +|D-15|
        qw=(6-i)**2 + abs(j-15)
        m.append(qw)
    i+=1
l=0
nac=rm
rew=[]
while(nac>=0):
    ac=rm-nac
    for i in m:
        if(i>=rm):
            l+=kr[0]*(ac) + nac*kr[1]
        elif(i<rm):
            if(i<=nac):
                l+=kr[1]*i
            elif(i>nac):
                l+=(i-nac)*kr[0] + nac*kr[1]
    if(l>rvn):
        print(ac)
        break
    nac-=1
    rew.append(l)
    l=0
if(nac<=0):
    print("Not possible")
    
    
    
    
    
    
    