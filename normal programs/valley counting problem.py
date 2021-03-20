# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:34:25 2019

@author: DELL
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 22:39:19 2019

@author: DELL
"""
'''COMPLETE SINGLY LINKED LIST MASTERED'''
import datetime as dt
class node:
    def __init__(self,data,place):
        self.data=data
        self.next=None
        self.place =dt.datetime.now()
class linkedlist():
    def __init__(self):
        self.head=None
    def insertathead(self,anothernode):
        temporary =self.head
        self.head=anothernode
        self.head.next = temporary
        del temporary
    def insertatpos(self,another_node,position):
        if(position ==0):
           self.insertathead(another_node)
           return            
        current_node = self.head
        current_position = 0
        previous_node = 0
        while(1):
           if(current_position == position-1):
              previous_node.next = another_node
              another_node.next = current_node
              break
           previous_node = current_node
           current_node=current_node.next
           current_position +=1
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
           self.new=self.place
           if(currentnode is None):
              break
           print(currentnode.data,end =':')
           #print("created at: ",llist.second.place)
           currentnode = currentnode.next
    def listlength(self):
        count =0
        length_node=self.head
        while(length_node is not None):
            count+=1
            length_node = length_node.next
        return count
    def deletelast(self):
        last_node = self.head
        while(last_node.next is not None):
            previous_node = last_node
            last_node = last_node.next
        previous_node.next = None
    def deletehead(self):
        first_node =self.head
        temp=self.head.next
        first_node.next=None
        self.head=temp
    def delanyposition(self,position):
        if(position<1 or position >llist.listlength()):
           print('please give a valid value')
        else:
           current_node = self.head
           current_position = 0
           previous_node = 0
           if(position==1):
              llist.deletehead()
           while(current_node.next!=None):
              if(current_position == position-1):
                 temp = current_node.next
                 previous_node.next = temp
                 current_node.next =None
                 break
              previous_node = current_node
              current_node=current_node.next
              current_position +=1
              if(current_node.next==None):
                 llist.deletelast()
llist =linkedlist()
print('enter "o/" to stop entering values')
while(1):
       code =input('plz enter the value: ')
       #print('enter "o/" to stop entering values')
       if(code!= 'o/'):
          second=node(code,dt.datetime.now())
          llist.insert(second)
       else:
          break
llist.printlist()
#m=llist.listlength()
'''def idoperation():
    print('enter "o/" to break execution and print the linked list')
    while(1):
       j=str(input( "press'i' to insert 'd' to delete a node starts from 1 to {}:".format(llist.listlength())))
       #print('enter "o/" to break execution')
       if(j=='o/'):
           break
       if(j=='i'):
          llist.insertatpos(node(input('insert the data of the new node: ')),int(input('enter position: ')))
          #llist.printlist() 
       if(j=='d'):     
          llist.delanyposition(int(input('enter position to be deleted: ')))
          #llist.printlist()
       else:
           print('INVALID VALUE ENTER AGAIN')'''
#a=input('do you want to insert delete operation press "y" to perform else press any key: ')
#if(a=='y' or a=="Y"):
#    idoperation()
#llist.printlist()