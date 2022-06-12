import matplotlib.pyplot as plt

year = [1950,1960,1970]
gdp = [67, 68, 80]

plt.bar(range(len(year)),gdp)

plt.xticks(range(len(year)),year)
plt.show()
