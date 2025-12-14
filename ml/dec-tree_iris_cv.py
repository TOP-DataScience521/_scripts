from matplotlib import pyplot as plt
from numpy import append, concatenate
from numpy.random import default_rng
from pandas import DataFrame, Series
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

from itertools import pairwise
from pathlib import Path
from sys import path


def k_fold_split(data, k):
    fold_len, res = divmod(data.shape[0], k)
    slices_idx = [0]
    acc = 0
    for fl, res_add in zip([fold_len]*k, [1]*res + [0]*(k-res)):
        acc += fl + res_add
        slices_idx.append(acc)
    folds = []
    for i, j in pairwise(slices_idx):
        folds.append(data[i:j])
    return folds


figures_path = Path(path[0]) / 'dec_tree output'


raw_data = load_iris()

data = append(raw_data.data, raw_data.target.reshape(-1, 1), axis=1)
default_rng(seed=1).shuffle(data)

data = DataFrame(
    data,
    columns=raw_data.feature_names+['class']
)
data['class'] = data['class'].astype(int)

# >>> data.shape
# (150, 5)


k = 5

folds = k_fold_split(data.values, k)

# >>> [fold.shape for fold in folds]
# [(30, 5), (30, 5), (30, 5), (30, 5), (30, 5)]

accuracies = []
for i in range(k):
    train = concatenate(folds[:i] + folds[i+1:])
    test = folds[i]
    
    x_train, y_train = train[:, :-1], train[:, -1]
    x_test, y_test = test[:, :-1], test[:, -1]
    
    model = DecisionTreeClassifier(criterion='entropy')
    model.fit(x_train, y_train)
    
    y_pred = model.predict(x_test)
    accuracies.append(accuracy_score(y_test, y_pred))

accuracy_mean = sum(accuracies) / len(accuracies)
print(f'{accuracy_mean:.1%}')
# 94.0%

