# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 17:50:54 2019

@author: DELL
"""
d={}
q=0
for i in range(1,int(input("please enter the number of center: "))+1):
    l=int((input("plz enter the number of seats at centre {}: ".format(i))))
    d[i]=l
    q+=l
print(q)
count=0
for i in range(int(input("please enter the number of students"))):
    if(i>q):
       count+=(q-(i+1))
       break
    m=int(input("enter the choice"))
    for _ in d.keys():
        #print(_)
        if(_ == m):
            #print("im here")
            
            if(d[_]==0):
                #print("im in zero case")
                d[_+1]=d[_+1]-1
                count+=1
            elif(d[_]!=0):
                #print("im in non zero case")
                d[_]=d[_]-1
            else:
                count+=1
print(d)
print("number of student not getting preffered choice",count)