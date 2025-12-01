from matplotlib import colormaps
from matplotlib import pyplot as plt
from numpy import array

from ts_init import births, passengers, online, script_dir


periods = [0, 2, 4, 6, 12]
cmap = colormaps['YlOrBr']
colors = [
    cmap(i/len(periods))
    for i in range(len(periods))
]
lines_width = [2] + [1]*(len(periods)-2) + [2]


fig = plt.figure(figsize=(25, 8))
axs = fig.subplots()

for per, color, lw in zip(periods, colors, lines_width):
    axs.plot(passengers.index, passengers.shift(per).values.flat, c=color, lw=lw)

fig.savefig(script_dir / 'time_series output/passengers_shifted.png')



data = {
    35: births.iloc[:, 0],
    25: passengers.iloc[:, 0],
    40: online.iloc[:, 0],
}
autocorrs = {}
for right, ts in data.items():
    coeffs = []
    for per in range(right):
        coeffs.append(ts.corr(ts.shift(per), method='kendall'))
    autocorrs[ts.name] = coeffs


for ts_name, coeffs in autocorrs.items():
    
    fig = plt.figure(figsize=(10, 7))
    axs = fig.subplots()
    
    for x, coeff in enumerate(coeffs):
        axs.vlines(x, 0, coeff, colors='#000')
        axs.scatter(x, coeff, s=40, c='#1f77b4')
        axs.set(ylim=(-1.05, 1.05))
    
    fig.savefig(script_dir / f'time_series output/{ts_name}_autocorr.png')

