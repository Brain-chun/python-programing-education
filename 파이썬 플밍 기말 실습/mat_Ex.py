import matplotlib.pyplot as plt

x=[x for x in range(20)]
y=[x**2 for x in range(20)]
z=[x**3 for x in range(20)]

plt.plot(x,x,label='1')
plt.plot(x,y,label='2')
plt.plot(x,z,label='3')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title('My Plot')
plt.legend()
plt.show()
