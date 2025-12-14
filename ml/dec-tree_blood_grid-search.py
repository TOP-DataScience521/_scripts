from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier, plot_tree

from blood_init import blood, x, y, figures_path


# tree_max = DecisionTreeClassifier(criterion='entropy')
# tree_max.fit(x, y)
# 
# fig = plt.figure(figsize=(100, 70))
# axs = fig.subplots()
# 
# plot_tree(tree_max, feature_names=blood.columns, ax=axs)
# 
# fig.savefig(figures_path / 'blood_max.png')


grid = GridSearchCV(
    estimator=DecisionTreeClassifier(criterion='entropy'),
    param_grid={
        'max_depth': range(2, 22),
        'min_samples_leaf': range(1, 25),
    },
    scoring='accuracy',
    cv=7,
    verbose=1,
    n_jobs=-1
)
grid.fit(x, y)


fig = plt.figure(figsize=(10, 7))
axs = fig.subplots()

plot_tree(grid.best_estimator_, feature_names=blood.columns, ax=axs)

fig.savefig(figures_path / 'blood_best.png')

