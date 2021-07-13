# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 17:16:20 2021

@author: 0555H9744
"""

f=open("Read.txt","a")
#content=f.read()
#print(content)
f.write("Hi hello")
# for line in f:
#     print(line)
f.close()
f=open("Read.txt")
for line in f:
     print(line)