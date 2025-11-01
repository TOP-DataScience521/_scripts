from pandas import concat, DataFrame, Series
from sklearn.datasets import load_breast_cancer


data_raw = load_breast_cancer()

data = DataFrame(data_raw['data'], columns=data_raw['feature_names'])
target = Series(data_raw['target'], name='target')

data_all = concat([data, target], axis=1)

# >>> data_all.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 569 entries, 0 to 568
# Data columns (total 31 columns):
#  #   Column                   Non-Null Count  Dtype
# ---  ------                   --------------  -----
#  0   mean radius              569 non-null    float64
#  1   mean texture             569 non-null    float64
#  2   mean perimeter           569 non-null    float64
#  3   mean area                569 non-null    float64
#  4   mean smoothness          569 non-null    float64
#  5   mean compactness         569 non-null    float64
#  6   mean concavity           569 non-null    float64
#  7   mean concave points      569 non-null    float64
#  8   mean symmetry            569 non-null    float64
#  9   mean fractal dimension   569 non-null    float64
#  10  radius error             569 non-null    float64
#  11  texture error            569 non-null    float64
#  12  perimeter error          569 non-null    float64
#  13  area error               569 non-null    float64
#  14  smoothness error         569 non-null    float64
#  15  compactness error        569 non-null    float64
#  16  concavity error          569 non-null    float64
#  17  concave points error     569 non-null    float64
#  18  symmetry error           569 non-null    float64
#  19  fractal dimension error  569 non-null    float64
#  20  worst radius             569 non-null    float64
#  21  worst texture            569 non-null    float64
#  22  worst perimeter          569 non-null    float64
#  23  worst area               569 non-null    float64
#  24  worst smoothness         569 non-null    float64
#  25  worst compactness        569 non-null    float64
#  26  worst concavity          569 non-null    float64
#  27  worst concave points     569 non-null    float64
#  28  worst symmetry           569 non-null    float64
#  29  worst fractal dimension  569 non-null    float64
#  30  target                   569 non-null    int64
# dtypes: float64(30), int64(1)
# memory usage: 137.9 KB


