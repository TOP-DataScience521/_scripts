from numpy import array, linspace, sin
from numpy.random import default_rng
from matplotlib import pyplot as plt
from pandas import DataFrame
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor

from pathlib import Path
from sys import path


rnd = default_rng(seed=1)
figures_path = Path(path[0]) / 'dec_tree output'


def f(x, bias_scale=1):
    return x * sin(x), x * sin(x) + rnd.normal(size=x.shape, scale=bias_scale)


n = 201
k = 50
m = 30

x = linspace(-10, 10, n)
f_true, f_bias = f(x)
data = DataFrame({'x': x, 'f_true': f_true, 'f_bias': f_bias})


predictions1 = []
for _ in range(k):
    bootstrap_k = rnd.choice(data, size=int(0.6*n))
    x_k = bootstrap_k[:, 0]
    f_k = bootstrap_k[:, -1]
    
    model_k = DecisionTreeRegressor(
        criterion='squared_error',
        max_depth=None,
        min_samples_leaf=1,
    ).fit(
        x_k.reshape(-1, 1), 
        f_k.reshape(-1, 1)
    )
    predictions1.append(model_k.predict(x.reshape(-1, 1)))
predictions1_mean = array(predictions1).mean(axis=0)
mse1 = mean_squared_error(f_true, predictions1_mean)
print(f'{mse1 = :.3f}')


predictions2 = []
model_bagging = BaggingRegressor(
    estimator=DecisionTreeRegressor(
        criterion='squared_error',
        max_depth=None,
        min_samples_leaf=1,
    ),
    n_estimators=k,
    max_samples=0.6,
    bootstrap=True,
    n_jobs=-1,
    random_state=1
)
model_bagging.fit(
    x.reshape(-1, 1), 
    f_bias
)
for model_k in model_bagging.estimators_:
    predictions2.append(model_k.predict(x.reshape(-1, 1)))
predictions2_mean = model_bagging.predict(x.reshape(-1, 1))
mse2 = mean_squared_error(f_true, predictions2_mean)
print(f'{mse2 = :.3f}')


predictions3 = []
for _ in range(m):
    model_bagging_m = BaggingRegressor(
        estimator=DecisionTreeRegressor(
            criterion='squared_error',
            max_depth=None,
            min_samples_leaf=1,
        ),
        n_estimators=k,
        max_samples=0.6,
        bootstrap=True,
        n_jobs=-1
    )
    model_bagging_m.fit(
        x.reshape(-1, 1), 
        f_bias
    )
    predictions3.append(model_bagging_m.predict(x.reshape(-1, 1)))
predictions3_mean = array(predictions3).mean(axis=0)
mse3 = mean_squared_error(f_true, predictions3_mean)
print(f'{mse3 = :.3f}')


fig = plt.figure(figsize=(21, 7))
axs = fig.subplots(1, 3)

axs[0].plot(x, f_true, lw=3, color='#000')
axs[0].scatter(x, f_bias, s=10, color='#fffacd')

axs[1].plot(x, f_true, '--k', lw=3)
for pred in predictions1:
    axs[1].plot(x, pred, lw=0.5, color='#ee82ee', alpha=0.2)
axs[1].plot(x, predictions1_mean, lw=2, color='#ffa500')

axs[2].plot(x, f_true, '--k', lw=3)
for pred in predictions2:
    axs[2].plot(x, pred, lw=0.5, color='#ee82ee', alpha=0.2)
axs[2].plot(x, predictions2_mean, lw=2, color='#ffa500')

fig.savefig(figures_path / 'bagging_synth.png')


fig = plt.figure(figsize=(14, 7))
axs = fig.subplots(1, 2)

axs[0].plot(x, f_true, lw=3, color='#000')
axs[0].scatter(x, f_bias, s=10, color='#fffacd')

axs[1].plot(x, f_true, '--k', lw=3)
for pred in predictions3:
    axs[1].plot(x, pred, lw=0.5, color='#ee82ee', alpha=0.2)
axs[1].plot(x, predictions3_mean, lw=2, color='#ffa500')

fig.savefig(figures_path / 'bagging_synth_cascade.png')

