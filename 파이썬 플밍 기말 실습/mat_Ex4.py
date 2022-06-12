import matplotlib.pyplot as plt
import numpy as np

bins= 10

x= np.random.randn(1000)
y = np.random.randn(1000)

plt.hist(x,bins,color ='red')
plt.hist(y, bins, color='blue',alpha=0.5)
plt.show()
