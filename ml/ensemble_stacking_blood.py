from sklearn.ensemble import StackingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from blood_init import x, y


x_params = x.describe()
x_norm = (x - x_params.loc['mean']) / x_params.loc['std']

x_train, x_test, y_train, y_test = train_test_split(
    x_norm, y,
    test_size=0.13,
    random_state=1
)
# >>> x_train.shape, y_train.shape
# ((650, 4), (650,))
# >>>
# >>> x_test.shape, y_test.shape
# ((98, 4), (98,))


ensemble = StackingClassifier(
    # лучше всего добавлять в стэк антагонистичные модели
    estimators=[
        ('tree', DecisionTreeClassifier(max_depth=3, min_samples_leaf=16)),
        ('svc', SVC(C=0.75, kernel='rbf', max_iter=-1)),
    ],
    # по умолчанию LogisticRegression
    final_estimator=None,
    cv=6,
    n_jobs=1,
)
ensemble.fit(x_train, y_train)
y_pred = ensemble.predict(x_test)

acc = accuracy_score(y_test, y_pred)
print(f'доля верных ответов: {acc:.3%}')

