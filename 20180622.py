import numpy as np

players = [[170,76.4],[183,86.2],[181,78.5],[176,80.1]]
c=[]
a = np.array(players)
print("몸무게가 80 이상인 선수 정보")
b=a[:,1]>=80
for i in range(4):
    if b[i]==True:
        c.append(list(a[i]))
print(c)    

c=[]
a = np.array(players)
print("키가 180 이상인 선수 정보")
b=a[:,0]>=180
for i in range(4):
    if b[i]==True:
        c.append(list(a[i]))
print(c)  
