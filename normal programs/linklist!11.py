# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 22:39:19 2019

@author: DELL
"""
'''GOOD CODE TO SOLVE LINKED LIST'''
from  desktop.playing import nwe
ll=nwe()
class node:
    def __init__(self,data):
        self.data=ll.enter()
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,newnode):
        if(self.head==None):
            self.head=newnode
        else:
            lastnode = self.head
            while(True):
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            lastnode.next = newnode
    def printlist(self):
        currentnode = self.head
        while(1):
           if(currentnode is None):
              break
           print(currentnode.data)
           currentnode = currentnode.next
llist =linkedlist()
while(1):
       print("To stop enter 'none'")
       code =input('plz enter the node: ')
       if(code!= 'none'):
          second=node(code)
          llist.insert(second)
       else:
          break
llist.printlist()
   