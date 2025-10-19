from matplotlib import pyplot as plt
from pandas import read_csv

from pathlib import Path
from sys import path


script_dir = Path(path[0])

data = read_csv(script_dir / 'boston.csv', comment='#')


# по умолчанию метод DataFrame.corr() вычисляет коэффициент линейной корреляции Пирсона
corr_pearson_matrix = data.corr()
corr_spearman_matrix = data.corr('spearman')


fig = plt.figure(figsize=(42, 42), dpi=200)
axs = fig.subplots(len(data.columns), len(data.columns))

for i, var1 in enumerate(data.columns):
    for j, var2 in enumerate(data.columns):
        axs[i,j].scatter(data[var1], data[var2], s=4)
        axs[i,j].set(
            title=f'{var1}–{var2}: cp={corr_pearson_matrix.loc[var1, var2]:.2f}, cs={corr_spearman_matrix.loc[var1, var2]:.2f}',
            xticks=[],
            yticks=[],
        )

fig.savefig(script_dir / 'boston_graph.png')


