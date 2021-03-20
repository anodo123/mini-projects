# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:44:32 2019

@author: DELL
"""
import socket
import datetime as dt
import json
import hashlib
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.money =int(input("enter the money involved:"))
        self.previous = dt.datetime.now()
        block =str(data)+str(self.money)+str(self.previous)
        block_string = json.dumps(block, sort_keys=True).encode()
        self.hash_value =  hashlib.sha256(block_string).hexdigest()
class doublylinkedlist:
    def __init__(self):
        self.head = None
    def append(self,data):
        if(self.head is None):
              new_node=node(data,)
              print("created at:",new_node.previous)
              self.head = new_node
              
        else:
            new_node = node(data)
            lastnode = self.head
            while(True):
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            lastnode.next = new_node
            new_node.previous = dt.datetime.now()
            print("created at:",new_node.previous)
            #print(lastnode.next)
    def insertathead(self,data):
        anothernode = node(data)
        temporary =self.head
        self.head=anothernode
        self.head.next = temporary
        self.head.previous = None
        del temporary
    def insertatanypos(self,data,position):
        another_node = node(data)
        if(position ==0):
           self.insertathead(another_node)
           return            
        current_node = self.head
        current_position = 0
        previous_node = 0
        while(1):
           if(current_position == position-1):
              previous_node.next = another_node
              another_node.previous = previous_node
              print("previous address:",another_node.previous)
              another_node.next = current_node
              print("next address:",another_node.next)
              break
           previous_node = current_node
           current_node=current_node.next
           current_position +=1
    def listlength(self):
        count =0
        length_node=self.head
        while(length_node is not None):
            count+=1
            length_node = length_node.next
        return count 
    def deletehead(self):
        first_node =self.head
        temp=self.head.next
        first_node.next=None
        temp.previous = None
        self.head=temp
    def deletelast(self):
        last_node = self.head
        while(last_node.next is not None):
            previous_node = last_node
            last_node = last_node.next
        previous_node.next = None
    def delanyposition(self,position):
        if(position<1 or position >dlist.listlength()):
           print('please give a valid value')
        else:
           current_node = self.head
           current_position = 0
           previous_node = 0
           if(position==1):
              dlist.deletehead()
           while(current_node.next!=None):
              if(current_position == position-1):
                 temp = current_node.next
                 previous_node.next = temp
                 current_node.next =None
                 current_node.previous = None
                 temp.previous = previous_node
                 print('delete at any pos',temp.previous)
                 print("delete2",temp)
                 break
              previous_node = current_node
              current_node=current_node.next
              current_position +=1
              if(current_node.next==None):
                 dlist.deletelast()
    '''def prepend(self,data):
        if self.head is None:
            new_node = node(data)
            new_node.previous = None
            self.head = new_node
        else:
            new_node = node(data)
            self.head.previous = new_node
            new_node.next = self.head
            print(new_node.next)
            self.head = new_node
            new_node.previous = None
            print(self.head.previous)'''
    def printlist(self):
        curr =self.head
        while(curr):
            print("                                          ",curr.previous)
            print("Name of the beneficiary:",curr.data)       
            print(' ')                                        
            print("Money recieved in Rs.",curr.money)             
            #hostname = socket.gethostname()             
            IPAddr = socket.getfqdn()                            
            #print("Name of device :",hostname)                 
            print("                                           Device Name :",IPAddr)
            print(" ")
            print("hash value    :",curr.hash_value)            
            curr=curr.next
dlist=doublylinkedlist()
print('enter "o/" to stop entering values')
while(1):
       code =input('plz enter the money: ')
       #print('enter "o/" to stop entering values')
       if(code!= 'o/'):
          dlist.append(code)
       else:
          break
dlist.printlist()
