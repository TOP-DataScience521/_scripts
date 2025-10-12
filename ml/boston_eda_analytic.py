from pandas import read_csv

from pathlib import Path
from sys import path


script_dir = Path(path[0])

data = read_csv(script_dir / 'boston.csv', comment='#')

# >>> data.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 506 entries, 0 to 505
# Data columns (total 14 columns):
#  #   Column   Non-Null Count  Dtype
# ---  ------   --------------  -----
#  0   CRIM     506 non-null    float64
#  1   ZN       506 non-null    float64
#  2   INDUS    506 non-null    float64
#  3   CHAS     506 non-null    float64
#  4   NOX      506 non-null    float64
#  5   RM       506 non-null    float64
#  6   AGE      506 non-null    float64
#  7   DIS      506 non-null    float64
#  8   RAD      506 non-null    float64
#  9   TAX      506 non-null    float64
#  10  PTRATIO  506 non-null    float64
#  11  B        506 non-null    float64
#  12  LSTAT    506 non-null    float64
#  13  MEDV     506 non-null    float64
# dtypes: float64(14)
# memory usage: 55.5 KB


with open(script_dir / 'boston_analytic.txt', 'w', encoding='utf-8') as fileout:
    for col in data:
        print(
            data[col].describe(),
            data[col].value_counts(sort=False).sort_index(),
            data[col].sort_values()[:10],
            data[col].sort_values()[-10:],
            sep='\n'*2,
            end='\n'*3,
            file=fileout,
        )

