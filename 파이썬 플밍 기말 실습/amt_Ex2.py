import matplotlib.pyplot as plt
import numpy as np

year = [1960,1970,1980]
ko=[130,1000,3000]
jp=[200,1500,2500]

x= np.arange(len(year))

plt.bar(x,ko,width=0.25)
plt.bar(x+0.3,jp,width = 0.25)
plt.xticks(x,year)

plt.show()
