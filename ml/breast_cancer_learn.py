from pandas import DataFrame
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from breast_cancer_init import data, target


# >>> data.shape, target.shape
# ((569, 30), (569,))

# >>> target.value_counts()
# target
# 1    357
# 0    212
# Name: count, dtype: int64

# 0 — злокачественная (malignant)
# 1 — доброкачественная (benign)


effect_vars = set(['worst perimeter', 'worst radius', 'worst area', 'worst concave points', 'mean concave points', 'mean perimeter', 'mean area', 'mean concavity', 'mean radius', 'area error', 'worst concavity', 'worst concave points', 'worst perimeter', 'mean concave points', 'worst radius', 'mean perimeter', 'worst area', 'mean radius', 'mean area', 'mean concavity', 'worst concavity', 'mean compactness'])

x_train, x_test, y_train, y_test = train_test_split(
    data.loc[:, list(effect_vars)],
    target,
    test_size=0.2,
    random_state=1
)

x_train_norm = (x_train - x_train.describe().loc['mean', :]) / x_train.describe().loc['std', :]
x_test_norm = (x_test - x_test.describe().loc['mean', :]) / x_test.describe().loc['std', :]

# >>> x_train.shape, y_train.shape
# ((455, 12), (455,))

# >>> x_test.shape, y_test.shape
# ((114, 12), (114,))


model = LogisticRegression()

model.fit(x_train_norm, y_train)

y_pred = model.predict(x_test_norm)

res_compare = DataFrame({
    'pred': y_pred,
    'test': y_test,
})

print(res_compare)

