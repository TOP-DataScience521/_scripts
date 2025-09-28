from matplotlib import pyplot as plt
from numpy import array, average, corrcoef, cov, linspace
from pandas import DataFrame


corr_table = DataFrame(
    {
         60: [3,  5,  0,  0,  0, 0],
         70: [0, 12, 11,  0,  0, 0],
         80: [0,  3, 28,  4,  0, 0],
         90: [0,  0,  3, 13,  4, 0],
        100: [0,  0,  0,  2, 10, 2],
    },
    index=range(25, 51, 5)
)
# >>> corr_table
#     60   70   80   90   100
# 25    3    0    0    0    0
# 30    5   12    3    0    0
# 35    0   11   28    3    0
# 40    0    0    4   13    2
# 45    0    0    0    4   10
# 50    0    0    0    0    2

# >>> corr_table.columns.to_numpy()
# array([ 60,  70,  80,  90, 100])
# >>>
# >>> corr_table.index.to_numpy()
# array([25, 30, 35, 40, 45, 50])

X_distr = array([corr_table.columns, corr_table.sum(axis=0)])

# >>> X_distr
# array([[ 60,  70,  80,  90, 100],
#        [  8,  23,  35,  20,  14]])
# >>>
# >>> average(X_distr[0], weights=X_distr[1])
# np.float64(80.9)

X = array([
    X_distr[0][i]
    for i in range(len(X_distr[0]))
    for _ in range(X_distr[1][i])
])
# >>> X
# array([ 60,  60,  60,  60,  60,  60,  60,  60,  70,  70,  70,  70,  70,
#         70,  70,  70,  70,  70,  70,  70,  70,  70,  70,  70,  70,  70,
#         70,  70,  70,  70,  70,  80,  80,  80,  80,  80,  80,  80,  80,
#         80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,
#         80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,
#         80,  90,  90,  90,  90,  90,  90,  90,  90,  90,  90,  90,  90,
#         90,  90,  90,  90,  90,  90,  90,  90, 100, 100, 100, 100, 100,
#        100, 100, 100, 100, 100, 100, 100, 100, 100])
# >>>
# >>> len(X)
# 100
# >>>
# >>> X.mean()
# np.float64(80.9)

Y_distr = array([corr_table.index, corr_table.sum(axis=1)])

# >>> Y_distr
# array([[25, 30, 35, 40, 45, 50],
#        [ 3, 20, 42, 19, 14,  2]])
# >>>
# >>> average(Y_distr[0], weights=Y_distr[1])
# np.float64(36.35)

Y = array([
    corr_table.index[j]
    for j in range(len(Y_distr[0]))
    for _ in range(Y_distr[1][j])
])
# >>> Y
# array([25, 25, 25, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30,
#        30, 30, 30, 30, 30, 30, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35,
#        35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35,
#        35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 40, 40, 40,
#        40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 45,
#        45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 50, 50])
# >>>
# >>> len(Y)
# 100
# >>>
# >>> Y.mean()
# np.float64(36.35)

xy_means = array([
    sum(corr_table.index * corr_table[x_val]) / corr_table[x_val].sum()
    for x_val in corr_table
])

# >>> xy_means
# array([28.125     , 32.39130435, 35.14285714, 40.25      , 45.        ])

corr_moment = sum(
    sum(x_val * corr_table.index * corr_table.loc[:, x_val])
    for x_val in corr_table
) / corr_table.sum().sum() - X.mean() * Y.mean()

corr_coef = corr_moment / (X.std() * Y.std())

corr_moment_2 = cov(X, Y)
corr_coef_2 = corrcoef(X, Y)

slope = corr_moment / X.var()
intercept = Y.mean() - slope * X.mean()


fig = plt.figure(figsize=(6, 5), dpi=150)
axs = fig.subplots()

xy_scat = array([
    (x_val, y_val)
    for x_val in corr_table.columns
    for y_val in corr_table.index
    if corr_table.loc[y_val, x_val]
]).T

# >>> xy_scat
# array([[ 60,  60,  70,  70,  80,  80,  80,  90,  90,  90, 100, 100, 100],
#        [ 25,  30,  30,  35,  30,  35,  40,  35,  40,  45,  40,  45,  50]])

x_regr = linspace(X_distr[0].min(), X_distr[0].max(), 41)
y_regr = slope * x_regr + intercept

axs.set(
    xticks=X_distr[0],
    yticks=Y_distr[0],
)
axs.scatter(*xy_scat)
axs.scatter(X.mean(), Y.mean(), c='#dd1111', marker='o')
axs.plot(X_distr[0], xy_means, '-Dy')
axs.plot(x_regr, y_regr, c='#000', lw=2)

fig.show()

