from matplotlib import pyplot as plt
from matplotlib import rcParams
from numpy import linspace
from numpy.random import default_rng


# точки графика распределения y1(x1)
x1 = linspace(-10, 10, 41)
y1 = default_rng().normal(size=x1.shape)

# точки графика распределения y2(x2)
x2 = linspace(1, 100, 100)
y2 = default_rng().uniform(-5, 5, size=x2.shape)


fig = plt.figure(figsize=(12, 6))
axs = fig.subplots(1, 2)

axs[0].scatter(x1, y1, s=rcParams['lines.markersize']**3, marker='^')
axs[1].scatter(x2, y2, c='#3dd')
axs[1].xaxis.set_visible(False)

fig.show()

