# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:57:58 2020

@author: DELL
"""

class hello:
    def __init__(self):
        self.first_data=int(input())
        self.second_data=int(input())
    def avg(self):
        m= (self.first_data + self.second_data)/2
        return m
s1=hello()
print(s1.__dict__)
    
    
    