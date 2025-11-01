from pandas import concat, DataFrame
from sklearn.preprocessing import OneHotEncoder

from categorical1 import data


columns_mask = ['lat', 'lng', 'capital', 'population']
rows_mask = [True]*data.shape[0]

data_filt = data.loc[rows_mask, columns_mask]

# >>> data_filt['capital'].value_counts(dropna=False)
# capital
# NaN        89
# admin      81
# minor      66
# primary     1
# Name: count, dtype: int64


# one-hot encoding

#          lat      lng  capital  population
# 0    55.7558  37.6172  primary  17332000.0
# 1    59.9375  30.3086    admin   5384342.0
# 2    55.0500  82.9500    admin   1625631.0
# 3    56.8356  60.6128    minor   1468833.0
# ...
# 235  56.5183  84.8369      NaN      2914.0

#          lat      lng  cap_na  cap_min  cap_reg  cap_prim  population
# 0    55.7558  37.6172       0        0        0         1  17332000.0
# 1    59.9375  30.3086       0        0        1         0  5384342.0
# 2    55.0500  82.9500       0        0        1         0  1625631.0
# 3    56.8356  60.6128       0        1        0         0  1468833.0
# ...
# 235  56.5183  84.8369       1        0        0         0  2914.0

# primary -> 0001
# admin   -> 0010
# minor   -> 0100
# NaN     -> 1000


encoder = OneHotEncoder(sparse_output=False)
encoder.fit(data_filt.loc[:, ['capital']])
capital_codes = encoder.transform(data_filt.loc[:, ['capital']])

# >>> capital_codes.shape
# (237, 4)

# >>> encoder.categories_
# [array(['admin', 'minor', 'primary', nan], dtype=object)]
# >>>
# >>> capital_codes[:5, :]
# array([[0., 0., 1., 0.],
#        [1., 0., 0., 0.],
#        [1., 0., 0., 0.],
#        [1., 0., 0., 0.],
#        [1., 0., 0., 0.]])
# >>>

a = data_filt.loc[:, ['lat', 'lng']]
b = DataFrame({
    'cap_na': capital_codes.T[3],
    'cap_min': capital_codes.T[1],
    'cap_reg': capital_codes.T[0],
    'cap_prim': capital_codes.T[2],
}, dtype='int8')
c = data_filt.loc[:, ['population']]

data_filt_enc = concat([a, b, c], axis=1)

