from matplotlib import pyplot as plt
from numpy import array, savetxt

from pathlib import Path
from random import randrange, shuffle, uniform
from sys import path


cluster1, cluster2, cluster3 = [], [], []

for _ in range(randrange(20, 30)):
    cluster1.append((uniform(1.5, 4), uniform(2.5, 4)))

for _ in range(randrange(25, 35)):
    cluster2.append((uniform(3, 5), uniform(-2, 0)))

for _ in range(randrange(15, 25)):
    cluster3.append((uniform(-1, 2), uniform(-0.25, 1.75)))

data = cluster1 + cluster2 + cluster3
shuffle(data)
data = array(data)


fig = plt.figure(figsize=(6, 6))
axs = fig.subplots()

x, y = data.T
axs.scatter(x, y)

fig.show()


savetxt(
    fname=Path(path[0]) / 'test_clusters.csv', 
    X=data, 
    fmt='%.1f', 
    delimiter=','
)

