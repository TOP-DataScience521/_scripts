from pandas import DataFrame, Series


df1 = DataFrame(
    data=[
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
)

# >>> df1
#    0   1   2   3
# 0  1   2   3   4
# 1  5   6   7   8
# 2  9  10  11  12
# >>>
# >>> df1.values
# array([[ 1,  2,  3,  4],
#        [ 5,  6,  7,  8],
#        [ 9, 10, 11, 12]])
# >>>
# >>> df1.columns
# RangeIndex(start=0, stop=4, step=1)
# >>>
# >>> df1.index
# RangeIndex(start=0, stop=3, step=1)

df2 = DataFrame(
    data=[
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ],
    columns=['col1', 'col2', 'col3', 'col4'],
    index=['row1', 'row2', 'row3']
)

# >>> df2
#       col1  col2  col3  col4
# row1     1     2     3     4
# row2     5     6     7     8
# row3     9    10    11    12
# >>>
# >>> df2.values
# array([[ 1,  2,  3,  4],
#        [ 5,  6,  7,  8],
#        [ 9, 10, 11, 12]])
# >>>
# >>> df2.columns
# Index(['col1', 'col2', 'col3', 'col4'], dtype='object')
# >>>
# >>> df2.index
# Index(['row1', 'row2', 'row3'], dtype='object')

df3 = DataFrame(
    data={
        'a': range(0, 5),
        'b': range(5, 10),
        'c': range(10, 15),
        'd': range(15, 20),
    }
)

# >>> df3
#    a  b   c   d
# 0  0  5  10  15
# 1  1  6  11  16
# 2  2  7  12  17
# 3  3  8  13  18
# 4  4  9  14  19

df4 = DataFrame(
    data=[
        Series(range(1, 11), name='ten1'),
        Series(range(11, 21), name='ten2'),
        Series(range(21, 31), name='ten3'),
    ]
)

# >>> df4
#        0   1   2   3   4   5   6   7   8   9
# ten1   1   2   3   4   5   6   7   8   9  10
# ten2  11  12  13  14  15  16  17  18  19  20
# ten3  21  22  23  24  25  26  27  28  29  30
# >>>
# >>> df4.T
#    ten1  ten2  ten3
# 0     1    11    21
# 1     2    12    22
# 2     3    13    23
# 3     4    14    24
# 4     5    15    25
# 5     6    16    26
# 6     7    17    27
# 7     8    18    28
# 8     9    19    29
# 9    10    20    30



# >>> df2['col1']
# row1    1
# row2    5
# row3    9
# Name: col1, dtype: int64
# >>>
# >>> df2['col2']
# row1     2
# row2     6
# row3    10
# Name: col2, dtype: int64
# >>>
# >>> df2['row1']
# KeyError: 'row1'



