import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(2,100)

fig, axs = plt.subplots(2,2,figsize=(5,5))

axs[0,0].plot(data[0],data[1])
axs[1,0].hist(data[0])
axs[0,1].hist2d(data[0],data[1])
axs[1,1].scatter(data[0],data[1])

plt.show()
