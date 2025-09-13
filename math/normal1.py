from matplotlib import pyplot as plt
from matplotlib import rcParams
from numpy import linspace
from numpy.random import default_rng

from time import sleep


rcParams['xtick.bottom'] = False
rcParams['xtick.labelbottom'] = False


N = 100
sigmas = linspace(0.01, 1.5, 150)


plt.ion()

fig = plt.figure(figsize=(6, 6), dpi=150)
axs = fig.subplots()

for sigma in sigmas:
    general = default_rng().normal(scale=sigma, size=N)
    
    axs.clear()
    axs.set(
        title=f'σ = {sigma:.2f}',
        ylim=(-7.5, 7.5),
    )
    axs.scatter(range(len(general)), general)
    axs.axhline(color='#dd1111')
    plt.draw()
    fig.canvas.flush_events()
    
    sleep(0.02)

plt.ioff()
plt.show()
