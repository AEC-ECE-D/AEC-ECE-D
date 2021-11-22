# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 09:58:58 2021

@author: admin
"""

import random
Data=[]
for ii in range(20):
    temp=random.randint(1,100)
    Data.append(temp)
print("the random values are:",Data)
summ=sum(Data)
avg=summ/20
print("the average value =",avg)
L =max (Data)
S =min (Data)
print("the largest number is",L)
print("the smallest number is",S)
Sort_Data=sorted(Data)
print("Sorted Numbers:",Sort_Data)
L2=Sort_Data[-2]
S2=Sort_Data[1]
print("the second largest number is",L2)
print("the second smallest number is",S2)
count=0
for ii in Data:
    if((ii%2)==0):
        count=count+1
print("No.of even elements=",count)



