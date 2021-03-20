# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:52:28 2020

@author: DELL
"""

class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)
    def preorder_print(self,start,traversal):
        """root-->left-->Right"""
        if(start):
            traversal = self.preorder_print(start.left,traversal)
            traversal+=(str(start.value) + "-")
            traversal = self.preorder_print(start.right,traversal)
        return traversal
    def inorder_print(self,start,traversal):
        """Left-->Root-->Right"""
        if(start):
            traversal = self.inorder_print(start.left,traversal)
            traversal+=(str(start.value) + "-")
            traversal = self.inorder_print(start.right,traversal)
        return traversal
    def postorder_print(self,start,traversal):
        """Left-->Right-->root"""
        if(start):
            traversal+=(str(start.value) + "-")
            traversal = self.postorder_print(start.left,traversal)
            traversal = self.postorder_print(start.right,traversal)
        return traversal
    def print_tree(self):
        while(1):
            traversal_type = str(input("enter 'pre' for preorder traversal.'post' for post order,'in' for in order traversal:\n  "))
            if (traversal_type == "in"):
                print(self.inorder_print(tree.root," "))
            elif (traversal_type == "pre"):
                print(self.preorder_print(tree.root," "))
            elif (traversal_type == "post"):
                print(self.postorder_print(tree.root," "))
            else:
                print("please enter proper value")
                return self.print_tree()
            b=str(input("enter 'Y' to traverse again else press any key: "))
            if(b == 'Y' or b == 'y' ):
                tree.print_tree()
            elif(b!="y" or b!="Y"):
                break
tree = BinaryTree(5)
b=tree.root
b.left= Node(2)
b.right= Node(4)
b.left.left = Node(8)
b.left.right = Node(43)
b.right.left = Node(453)
b.right.right = Node(555)
tree.print_tree()









