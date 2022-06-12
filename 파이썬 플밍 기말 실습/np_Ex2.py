import numpy as np

x=np.array([['a','b','c','d'],['c','c','g','h']])

a=np.array([[10,20,30],[10,20,30]])
b=np.array([[2,2,2],[1,2,3]])

c=[]

for i in x[x=='c']:
    if i==True:
        c.append(x[x=='c'])
