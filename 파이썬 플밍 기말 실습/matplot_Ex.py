import matplotlib.pyplot as plt
x=[x for x in range(-20,20)]
y=[2*t for t in x]
z=[2*t**2 for t in x]
k=[2*t**3 for t in x]

plt.plot(x,y,label='linear')

plt.plot(x,z,label='제곱')
plt.plot(x,k,label='123')
plt.legend()
plt.axis([-20,20,-20,20])
plt.show()
