from matplotlib import pyplot as plt
from pandas import DataFrame

from pathlib import Path
from sys import path

from breast_cancer_init import data, target


# значения категориальной переменной
# >>> target.value_counts()
# target
# 1    357
# 0    212
# Name: count, dtype: int64

# маски значений категориальной переменной
mask_0 = target == 0
mask_1 = target == 1

# значения порядковой переменной, которым сопоставлено значение 0 категориальной переменной
# >>> data.loc[mask_0, 'mean radius']
# 0      17.99
# 1      20.57
# 2      19.69
# 3      11.42
# 4      20.29
#        ...
# 563    20.92
# 564    21.56
# 565    20.13
# 566    16.60
# 567    20.60
# Name: mean radius, Length: 212, dtype: float64

# значения порядковой переменной, которым сопоставлено значение 1 категориальной переменной
# >>> data.loc[mask_1, 'mean radius']
# 19     13.540
# 20     13.080
# 21      9.504
# 37     13.030
# 46      8.196
#         ...
# 558    14.590
# 559    11.510
# 560    14.050
# 561    11.200
# 568     7.760
# Name: mean radius, Length: 357, dtype: float64


bins = 30
script_dir = Path(path[0])

fig = plt.figure(figsize=(8, 5))
axs = fig.subplots()

for var_name in data.columns:
    axs.clear()
    axs.hist(
        data.loc[mask_0, var_name], 
        bins=bins, 
        alpha=0.5,
        label='значение 0 категориальной переменной'
    )
    axs.hist(
        data.loc[mask_1, var_name], 
        bins=bins, 
        color='#ff7f0e88',
        label='значение 1 категориальной переменной'
    )
    axs.set(
        title=var_name,
        xlabel='значения порядковой переменной',
        ylabel='количество значений порядковой переменной в интервалах',
    )
    axs.legend()
    fig.savefig(script_dir / f'breast_cancer output/{var_name}.png')


