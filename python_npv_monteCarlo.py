# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 00:49:11 2019

@author: misaa
"""
import numpy as np
import pandas as pd

'''
# Begin Table
n0 = [-8100000,-306850.03,-75000,0,0]
n1 = [0,0,0,0,0]
n2 = [0,0,0,0,0]
n3 = [0,0,75000,0,6280000]

taxRate = .3

sales = np.random.normal(2100000,210000,3)
costs = np.random.normal(400000,40000,3)

n1[3] = (sales[0] - costs[0]) * (1 - taxRate)
n2[3] = (sales[1] - costs[1]) * (1 - taxRate)
n3[3] = (sales[2] - costs[2]) * (1 - taxRate)

n0.append(sum(n0))
n1.append(sum(n1))
n2.append(sum(n2))
n3.append(sum(n3))

table = pd.DataFrame((list(zip(n0,n1,n2,n3))),columns=[0,1,2,3],index=['NCS','FC','DNWC','OCF','ATS','CFFA'])
print(table)

CFFA = table.loc['CFFA']
print("NPV is: ",np.npv(.0615,CFFA))
'''
taxRate = .3

def revenue():
    s = np.random.normal(2100000,210000,3)
    return s

def expenses():
    c = np.random.normal(400000,40000,3)
    return c

x = 0
while x < 50:
    sales = revenue()
    print(sales)
    x+=1

y = 0
while y < 50:
    costs = expenses()
    print(costs)
    y+=1
    
Sales = pd.DataFrame(sales)
Costs = pd.DataFrame(costs)

def ocf():
    cashFlow = (Sales-Costs) * (1 - taxRate)
    return cashFlow
    
i = 0
while i < 50:
    a = ocf()
    print(a)
    i +=1

    



sales = []
costs = []

for x in range(0,499):
   sales = np.random.normal(2100000,210000,1)
   costs = np.random.normal(400000,400000,1)
   sales.append(x,sales(x))
   
print(sales)
'''
