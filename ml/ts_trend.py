from matplotlib import pyplot as plt
from pandas import Series

from ts_init import births, passengers, online, script_dir


widths_series = {
    # размеры окон для скользящих средних (ma — moving average)
    (3, 7, 14, 30): births,
    (2, 4, 6, 12): passengers,
    (4, 12, 24, 72, 168): online,
}

for widths, ts in widths_series.items():
    ts_ma = {w: Series([], name=f'ma_{w}') for w in widths}
    
    for window in widths:
        for i in range(0, len(ts)-window+1):
            dt_index = ts.index[i+window//2]
            ts_ma[window].loc[dt_index] = ts.iloc[i:i+window].mean().iloc[0]
    
    fig = plt.figure(figsize=(10, 3*len(widths)))
    axs = fig.subplots(len(widths), 1)
    
    for i, window in enumerate(widths):
        axs[i].plot(ts.index, ts.iloc[:, 0].values)
        axs[i].plot(ts_ma[window].index, ts_ma[window].values)
        axs[i].set(title=f'ширина окна = {window}')
    
    fig.savefig(script_dir / f'ts_{ts.columns[0]}_ma.png')



alpha = 0.2

births_expsm = [births.iloc[0, 0]]

for i in range(1, len(births.index)):
    births_expsm.append(alpha * births.iloc[i, 0] + (1 - alpha) * births_expsm[i-1])

births_expsm = Series(
    births_expsm,
    index=births.index, 
    name='exp_smooth_0.5'
)

fig = plt.figure(figsize=(15, 6))
axs = fig.subplots()

axs.plot(births.index, births.iloc[:, 0].values)
axs.plot(births_expsm.index, births_expsm.values)
axs.set(title=f'alpha = {alpha}')

fig.savefig(script_dir / f'ts_births_expsm.png')

