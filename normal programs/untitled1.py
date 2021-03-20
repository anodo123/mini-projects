# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:01:11 2019

@author: DELL
"""
class node(object):
    def __init__(self,value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
class binarytree(object):
    def __init__(self):
        self.root = None
    def insert(self,value):
        if(self.root == None):
            self.root = node(value)
        else:
            self._insert(value,self.root)
    def _insert(self,value,cur_node):
        if(value<cur_node.value):
            if(cur_node.left_child ==None):
                cur_node.left_child= node(value)
            else:
                self._insert(value,cur_node.left_child)
        elif(value>cur_node.value):
             if(cur_node.right_child ==None):
                cur_node.right_child= node(value)
             else:
                self._insert(value,cur_node.right_child)
        else:
            print("value is already in tree")
    def print_tree(self):
        if(self.root!=None):
            self._print_tree(self.root)
    def _print_tree(self,cur_node):
        if(cur_node is not None):
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)
    def height(self):
        if(self.root!=None):
           return self._height(self.root,0)
        else:
           return 0
    def _height(self,cur_node,cur_height):
        if cur_node==None: return cur_height
        left_height=self._height(cur_node.left_child,cur_height+1)
        right_height=self._height(cur_node.right_child,cur_height+1)
        return max(left_height,right_height)
    def search(self,value):
        if(self.root!=None):
            print("im called")
            return self._search(value,self.root)
        else:
            return False
    def _search(self,value,cur_node):
        print(cur_node.value)
        if(value == int(cur_node.value)):
            return True
        elif(value<cur_node.value and cur_node.left_child!=None):
            print(cur_node.value)
            return self._search(value,cur_node.left_child)
        elif(value>cur_node.value and cur_node.right_child!=None):
            print(cur_node.value)
            return self._search(value,cur_node.right_child) 
        else:
            return False
tree=binarytree()
while(1):
    a=input("insert value")
    if(a=="o/"):
        break
    else:
        tree.insert(a)
tree.print_tree()
print("tree height:"+str(tree.height()))
a=tree.search(input("enter the element to be searched"))
print("the element status in tree:{}".format(a))