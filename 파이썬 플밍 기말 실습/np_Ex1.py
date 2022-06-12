import numpy as np

p=[[170,76.4],[183,86.2],[181,78.5],[176,80.1]]

a=np.array(p)
c=[]
b=a[:,1]>=80

for i in range(4):
    if b[i]==True:
        c.append(list(a[i]))

print(c)
