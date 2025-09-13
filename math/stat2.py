from matplotlib import pyplot as plt
from matplotlib import rcParams
from numpy import arange, array
from numpy.random import default_rng


a = 5
σ = 0.7
N = 10**6
general = default_rng().normal(a, σ, N)
general_XY = array([arange(len(general)), general]).T

n = 100
sample_XY = default_rng().choice(general_XY, n)
sample = sample_XY.T[1]


# fig = plt.figure(figsize=(6, 6), dpi=150)
# axs = fig.subplots()
# 
# axs.scatter(*general_XY.T, s=3)
# axs.scatter(*sample_XY.T, s=18)
# 
# fig.show()


sample_mean = sample.mean()
sample_std_corr = sample.std(ddof=1)

γ = 0.95
print(
    f'\nдоверительная вероятность: {γ:.2f}'
    f'\nуровень надёжности: {1-γ:.2f}'
    f'\nколичество степеней свободы: {n-1}'
)
t_γ = float(input('критическая точка распределения: '))
ε = t_γ * sample_std_corr / n**0.5

print(
    f'\nсреднее выборочное: {sample_mean:.3f}'
    f'\nисправленное среднее квадратичное отклонение: {sample_std_corr:.3f}'
    f'\nошибка выборки: {ε:.3f}'
    f'\nдоверительный интервал: ({sample_mean-ε:.3f}; {sample_mean+ε:.3f})'
)

