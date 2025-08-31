from matplotlib import pyplot as plt

from pathlib import Path
from sys import path

# точки графика функции y(x) = x
x = range(10)
y = range(10)


fig = plt.figure(figsize=(10, 6))
axs = fig.subplots()

axs.plot(x, y)

fig.savefig(Path(path[0]) / 'graphics1.png')
fig.show()
fig.savefig(Path(path[0]) / 'graphics1_2.png', dpi=200)

