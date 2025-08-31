from pandas import Series


col1 = Series(data=[12, 0.79, 2.2, 5.5, 0.13])
col2 = Series(
    data=[12, 0.79, 2.2, 5.5, 0.13],
    index=['first', 'second', 'third', 'fourth', 'fifth']
)

# >>> col1
# 0    12.00
# 1     0.79
# 2     2.20
# 3     5.50
# 4     0.13
# dtype: float64
# >>>
# >>> col1.values
# array([12.  ,  0.79,  2.2 ,  5.5 ,  0.13])
# >>>
# >>> col1.index
# RangeIndex(start=0, stop=5, step=1)
# >>>
# >>> type(col1.index)
# <class 'pandas.core.indexes.range.RangeIndex'>
# >>>
# >>>
# >>> col2
# first     12.00
# second     0.79
# third      2.20
# fourth     5.50
# fifth      0.13
# dtype: float64
# >>>
# >>> col2.values
# array([12.  ,  0.79,  2.2 ,  5.5 ,  0.13])
# >>>
# >>> col2.index
# Index(['first', 'second', 'third', 'fourth', 'fifth'], dtype='object')
# >>>
# >>> type(col2.index)
# <class 'pandas.core.indexes.base.Index'>


# >>> col1.index[0]
# 0
# >>> col1.index[1]
# 1
# >>> col2.index[0]
# 'first'
# >>> col2.index[1]
# 'second'


# >>> col1
# 1    12.00
# 2     0.79
# 3     2.20
# 4     5.50
# 5     0.13
# dtype: float64
# >>>
# >>> col1.index
# Index(['1', '2', '3', '4', '5'], dtype='object')

# >>> col1.index = col2.index
# >>>
# >>> col1
# first     12.00
# second     0.79
# third      2.20
# fourth     5.50
# fifth      0.13
# dtype: float64
# >>>
# >>> col1.index
# Index(['first', 'second', 'third', 'fourth', 'fifth'], dtype='object')


# >>> col1.name = 'params'
# >>> col1
# first     12.00
# second     0.79
# third      2.20
# fourth     5.50
# fifth      0.13
# Name: params, dtype: float64


col3 = Series({'a': 10, 'b': 20, 'c': 30}, name='test_column')

# >>> col3
# a    10
# b    20
# c    30
# Name: test_column, dtype: int64
# >>>
# >>> col3.values
# array([10, 20, 30])
# >>>
# >>> col3.index
# Index(['a', 'b', 'c'], dtype='object')

