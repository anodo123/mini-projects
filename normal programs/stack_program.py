# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 10:19:22 2020

@author: DELL
"""

class stack:
    def __init__(self): 
        self.s=[]
    def push(self):
        while(1):
            g=str(input("enter the value:  "))
            if(g =="o/"):
               break
            else:
                self.s.append(g)
                print("To break enter 'o/'")
    def pop(self):
        if(len(self.s)==0):
            print("stack is empty")
            return None
        else:
            return self.s.pop(-1)
    def printlist(self):
        print(self.s)
s=stack()
s.push()
s.pop()
s.printlist()
class queue:
    def __init__(self): 
        self.s=[]
    def push(self):
        while(1):
            g=str(input("enter the value:  "))
            if(g =="o/"):
               break
            else:
                self.s.append(g)
                print("To break enter 'o/'")
    def pop(self):
        return self.s.pop(0)
    def print(self):
        print(self.s)
#g=queue()
#g.push()
#g.pop()
#g.print()
            
            
            