# -*- coding: utf-8 -*-
"""
Created on Wed May  5 21:52:27 2021

@author: 0555H9744
"""

class Employee(object):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def display(self):
        print(self.name)
        print(self.salary)
        
class Rabi(Employee):
    def __init__(self, name, salary,no):
        self.no=no
        self.name=name
        Employee.__init__(self, name, salary)

a=Rabi('osman',0,34)
a.display()    
        