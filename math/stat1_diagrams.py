from matplotlib import pyplot as plt
from numpy import array, histogram

from stat1 import *


# ширина каждого интервала
X_intervals_widths = [interval[1] - interval[0] for interval in X_intervals]
# высота столбцов гистограммы с нормировкой на ширину каждого интервала
h_intervals = [
    m_intervals[i] / X_intervals_widths[i]
    for i in range(len(X_intervals))
]

# то же самое средствами numpy
# X_intervals_widths_ = array(X_intervals).T[1] - array(X_intervals).T[0]
# h_intervals_ = array(m_intervals) / X_intervals_widths_


fig = plt.figure(figsize=(12, 6), dpi=150)
axs = fig.subplots(1, 2)

# гистограмма интервального ряда с самостоятельно рассчитанными параметрами столбцов
axs[0].bar(
    x=X_intervals_means,
    height=h_intervals,
    width=X_intervals_widths,
)

# гистограмма интервального ряда с автоматически рассчитанными параметрами столбцов
# правило отнесения пограничных частот при вычислении частот интервалов отличается от использованного ранее! (см. документацию numpy.histogram)
# axs[1].hist(x=sample, bins=5)
# axs[1].hist(x=X, weights=m, bins=5)

# столбчатая диаграмма дискретного ряда
axs[1].bar(x=X, height=m)

fig.show()

