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

# 0 — злокачественная (malignant) — отрицательный
# 1 — доброкачественная (benign)  — положительный


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
    'прогноз': y_pred,
    'факт': y_test,
})

# print(res_compare, end='\n\n')


def confusion_matrix(predicted, test):
    TN, TP, FN, FP = 0, 0, 0, 0
    for p, t in zip(predicted, test):
        # истинноотрицательный
        if p == t == 0:
            TN += 1
        # истинноположительный
        elif p == t == 1:
            TP += 1
        # ложноотрицательный
        elif p == 0 and t == 1:
            FN += 1
        # ложноположительный
        elif p == 1 and t == 0:
            FP += 1
    return DataFrame(
        [[TN, FP],
         [FN, TP]],
        columns=['прогноз: отрицательный', 'прогноз: положительный'],
        index=['факт: отрицательный', 'факт: положительный'],
    )

conf_matr = confusion_matrix(y_pred, y_test)

print(conf_matr, end='\n\n')
#                      прогноз: отрицательный  прогноз: положительный
# факт: отрицательный                      37                       5
# факт: положительный                       2                      70

(TN, FP), (FN, TP) = conf_matr.values


#                 TN + TP      
# accuracy = ————————————————— 
#            TN + FP + FN + TP 

accuracy = conf_matr.values.diagonal().sum() / conf_matr.sum().sum()

#               TP   
# precision = ——————— 
#             TP + FP 

precision = TP / (TP + FP)

#                 TN   
# specificity = ——————— 
#               TN + FP 

specificity = TN / (TN + FP)

#            TP   
# recall = ——————— 
#          TP + FN 

recall = TP / (TP + FN)

f1_score = 2 * precision * recall / (precision + recall)


print(
    f'{accuracy = :.2f}',
    f'ошибок второго рода: {FP}',
    f'{precision = :.2f}',
    f'{specificity = :.2f}',
    f'{recall = :.2f}',
    f'{f1_score = :.2f}',
    sep='\n'
)
# accuracy = 0.94
# ошибок второго рода: 5
# precision = 0.93
# specificity = 0.88
# recall = 0.97
# f1_score = 0.95

