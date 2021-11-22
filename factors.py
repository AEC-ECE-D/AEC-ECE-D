# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 10:03:46 2021

@author: admin
"""

data=int(input("Enter a number="))
list=[]
for ii in range(1,data+1):
    if(data%ii==0):
        list.append(ii)
print(list)