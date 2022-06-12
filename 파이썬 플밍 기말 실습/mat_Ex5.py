import matplotlib.pyplot as plt
import numpy as np

standard = np.random.randn(1000)
G1= 10+2*standard
G2 = -6 +3*standard

plt.figure(figsize=(10,6))
plt.hist(standard, bins=50,color='blue', alpha=0.5)
plt.hist(G1,bins=50,color='orange',alpha=0.5)
plt.hist(G2,bins=50,color='green',alpha=0.5)

plt.show()
