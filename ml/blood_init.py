from matplotlib import pyplot as plt
from pandas import DataFrame
from scipy.io.arff import loadarff

from itertools import pairwise
from pathlib import Path
from sys import path


script_dir = Path(path[0])
figures_path = script_dir / 'dec_tree output'

with open(script_dir / 'blood.arff', encoding='utf-8') as filein:
    data_raw = loadarff(filein)

blood = DataFrame(data_raw[0])

blood.columns = ['recency', 'frequency', 'monetary', 'time', 'donated']

blood.loc[blood['donated'] == b'1', 'donated'] = 0
blood.loc[blood['donated'] == b'2', 'donated'] = 1

blood = blood.astype(dtype=int)

x, y = blood.iloc[:, :-1], blood.iloc[:, -1]


if __name__ == '__main__':
    
    fig = plt.figure(figsize=(8, 8))
    axs = fig.subplots(2, 2)
    
    for k, (col1, col2) in enumerate(pairwise(list(x.columns) + [x.columns[0]])):
        i, j = divmod(k, 2)
        mask0, mask1 = y == 0, y == 1
        axs[i,j].scatter(x.loc[mask0, col1], x.loc[mask0, col2], s=10)
        axs[i,j].scatter(x.loc[mask1, col1], x.loc[mask1, col2], s=10)
        axs[i,j].set(xlabel=col1, ylabel=col2)
    
    fig.savefig(figures_path / 'blood_data.png')

