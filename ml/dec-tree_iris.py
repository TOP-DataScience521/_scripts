from graphviz import Source
from matplotlib import pyplot as plt
from pandas import DataFrame, Series
from sklearn.datasets import load_iris
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz

from pathlib import Path
from sys import path


figures_path = Path(path[0]) / 'dec_tree output'


raw_data = load_iris()
x = DataFrame(
    raw_data.data,
    columns=raw_data.feature_names
)
y = Series(
    raw_data.target,
    name='class'
)
# >>> x.shape
# (150, 4)
# >>>
# >>> y.shape
# (150,)


fig = plt.figure(figsize=(16, 16))
axs = fig.subplots(2, 2)

mask0 = y == 0
mask1 = y == 1
mask2 = y == 2

axs[0,0].scatter(x.loc[mask0, 'sepal length (cm)'], x.loc[mask0, 'sepal width (cm)'])
axs[0,0].scatter(x.loc[mask1, 'sepal length (cm)'], x.loc[mask1, 'sepal width (cm)'])
axs[0,0].scatter(x.loc[mask2, 'sepal length (cm)'], x.loc[mask2, 'sepal width (cm)'])
axs[0,0].set(xlabel='sepal length (cm)', ylabel='sepal width (cm)')
axs[0,1].scatter(x.loc[mask0, 'petal length (cm)'], x.loc[mask0, 'petal width (cm)'])
axs[0,1].scatter(x.loc[mask1, 'petal length (cm)'], x.loc[mask1, 'petal width (cm)'])
axs[0,1].scatter(x.loc[mask2, 'petal length (cm)'], x.loc[mask2, 'petal width (cm)'])
axs[0,1].set(xlabel='petal length (cm)', ylabel='petal width (cm)')
axs[1,0].scatter(x.loc[mask0, 'sepal length (cm)'], x.loc[mask0, 'petal length (cm)'])
axs[1,0].scatter(x.loc[mask1, 'sepal length (cm)'], x.loc[mask1, 'petal length (cm)'])
axs[1,0].scatter(x.loc[mask2, 'sepal length (cm)'], x.loc[mask2, 'petal length (cm)'])
axs[1,0].set(xlabel='sepal length (cm)', ylabel='petal length (cm)')
axs[1,1].scatter(x.loc[mask0, 'sepal length (cm)'], x.loc[mask0, 'petal width (cm)'])
axs[1,1].scatter(x.loc[mask1, 'sepal length (cm)'], x.loc[mask1, 'petal width (cm)'])
axs[1,1].scatter(x.loc[mask2, 'sepal length (cm)'], x.loc[mask2, 'petal width (cm)'])
axs[1,1].set(xlabel='sepal length (cm)', ylabel='petal width (cm)')

fig.savefig(figures_path / 'iris_effect-vars.png')


# >>> x.corr().round(2)
#                    sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
# sepal length (cm)               1.00             -0.12               0.87              0.82
# sepal width (cm)               -0.12              1.00              -0.43             -0.37
# petal length (cm)               0.87             -0.43               1.00              0.96
# petal width (cm)                0.82             -0.37               0.96              1.00

# >>> x.corrwith(y).round(2)
# sepal length (cm)    0.78
# sepal width (cm)    -0.43
# petal length (cm)    0.95
# petal width (cm)     0.96
# dtype: float64

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    random_state=3
)
# >>> x_train.shape, y_train.shape
# ((120, 4), (120,))
# >>>
# >>> x_test.shape, y_test.shape
# ((30, 4), (30,))


model_max = DecisionTreeClassifier(
    criterion='entropy',
    random_state=1,
)
model_min = DecisionTreeClassifier(
    criterion='entropy',
    min_samples_split=50,
    random_state=1,
)

model_max.fit(x_train, y_train)
model_min.fit(x_train, y_train)

Source(export_graphviz(model_max)).render(
    format='png', 
    outfile=figures_path/'iris_max.png'
)
Source(export_graphviz(model_min)).render(
    format='png', 
    outfile=figures_path/'iris_min.png'
)

y_pred_max = model_max.predict(x_test)
y_pred_min = model_min.predict(x_test)

acc_max = accuracy_score(y_test, y_pred_max)
acc_min = accuracy_score(y_test, y_pred_min)
print(
    f'максимальное дерево: {acc_max:.1%}',
    f'минимальное дерево: {acc_min:.1%}',
    sep='\n',
)


fig = plt.figure(figsize=(5,5))
axs = fig.subplots()

axs.scatter(x.loc[mask0, 'petal length (cm)'], x.loc[mask0, 'petal width (cm)'], s=20)
axs.scatter(x.loc[mask1, 'petal length (cm)'], x.loc[mask1, 'petal width (cm)'], s=20)
axs.scatter(x.loc[mask2, 'petal length (cm)'], x.loc[mask2, 'petal width (cm)'], s=20)

# вручную
# axs.axhspan(-1, 0.8, color='#1111d9', alpha=0.15)
# axs.axvspan(0, 4.75, 0.333, color='#d91111', alpha=0.15)
# axs.axvspan(4.75, 10, 0.333, color='#11d911', alpha=0.15)

axs.set(xlim=(0.9, 7.1), ylim=(-0.1, 2.6))

# класс для автоматического построения решающей плоскости
DecisionBoundaryDisplay.from_estimator(
    # модель, обученная на двух зависимых признаках
    DecisionTreeClassifier(
        criterion='entropy', 
        min_samples_split=50
    ).fit(
        x.loc[:, ['petal length (cm)', 'petal width (cm)']], 
        y
    ),
    x.loc[:, ['petal length (cm)', 'petal width (cm)']],
    ax=axs,
    xlabel='petal length (cm)',
    ylabel='petal width (cm)',
    alpha=0.3,
)

fig.savefig(figures_path / 'iris_min_surface.png')


