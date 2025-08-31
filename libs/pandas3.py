from pandas import DataFrame

from random import choice, uniform


vowels = 'AEIOU'
consonants = 'BCDFGHJKLMNPRSQTVWXYZ'


def rand_word() -> str:
    return f'{choice(consonants)}{choice(vowels)}{choice(consonants)}'


df = DataFrame(
    data={
        rand_word(): [
            round(uniform(1, 10), 4) 
            for _ in range(10)
        ]
        for _ in range(5)
    }
)

# >>> df
#       QAS     KAK     ROL     WEM     LOW
# 0  5.0307  6.4092  6.6762  8.9102  5.4705
# 1  3.7689  1.9093  1.8859  1.7767  5.5959
# 2  8.4284  7.8560  5.3405  9.2567  5.9261
# 3  5.0169  4.8533  3.6978  1.6115  3.9332
# 4  8.8328  4.6627  6.0551  2.5282  4.9852
# 5  5.9267  1.4243  9.9718  3.3000  9.5929
# 6  1.7010  1.1954  7.1716  3.4653  8.3125
# 7  2.5004  7.4380  3.7639  5.1351  5.5571
# 8  4.6083  4.2008  3.7603  1.6072  7.8129
# 9  4.2537  7.0992  9.9241  6.4532  7.9252
# >>>
# >>> df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10 entries, 0 to 9
# Data columns (total 5 columns):
#    # Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   QAS     10 non-null     float64
#  1   KAK     10 non-null     float64
#  2   ROL     10 non-null     float64
#  3   WEM     10 non-null     float64
#  4   LOW     10 non-null     float64
# dtypes: float64(5)
# memory usage: 532.0 bytes


# >>> df > 5
#      QAS    KAK    ROL    WEM    LOW
# 0   True   True   True   True   True
# 1  False  False  False  False   True
# 2   True   True   True   True   True
# 3   True  False  False  False  False
# 4   True  False   True  False  False
# 5   True  False   True  False   True
# 6  False  False   True  False   True
# 7  False   True  False   True   True
# 8  False  False  False  False   True
# 9  False   True   True   True   True
# >>>
# >>>
# >>> df[df > 5]
#       QAS     KAK     ROL     WEM     LOW
# 0  5.0307  6.4092  6.6762  8.9102  5.4705
# 1     NaN     NaN     NaN     NaN  5.5959
# 2  8.4284  7.8560  5.3405  9.2567  5.9261
# 3  5.0169     NaN     NaN     NaN     NaN
# 4  8.8328     NaN  6.0551     NaN     NaN
# 5  5.9267     NaN  9.9718     NaN  9.5929
# 6     NaN     NaN  7.1716     NaN  8.3125
# 7     NaN  7.4380     NaN  5.1351  5.5571
# 8     NaN     NaN     NaN     NaN  7.8129
# 9     NaN  7.0992  9.9241  6.4532  7.9252


# >>> df.index
# RangeIndex(start=0, stop=10, step=1)
# >>>
# >>>
# >>> df.index % 2 == 0
# array([ True, False,  True, False,  True, False,  True, False,  True,
#        False])
# >>>
# >>>
# >>> df.loc[df.index % 2 == 0]
#       QAS     KAK     ROL     WEM     LOW
# 0  5.0307  6.4092  6.6762  8.9102  5.4705
# 2  8.4284  7.8560  5.3405  9.2567  5.9261
# 4  8.8328  4.6627  6.0551  2.5282  4.9852
# 6  1.7010  1.1954  7.1716  3.4653  8.3125
# 8  4.6083  4.2008  3.7603  1.6072  7.8129
# >>>
# >>>
# >>> df.iloc[df.index % 2 == 0]
#       QAS     KAK     ROL     WEM     LOW
# 0  5.0307  6.4092  6.6762  8.9102  5.4705
# 2  8.4284  7.8560  5.3405  9.2567  5.9261
# 4  8.8328  4.6627  6.0551  2.5282  4.9852
# 6  1.7010  1.1954  7.1716  3.4653  8.3125
# 8  4.6083  4.2008  3.7603  1.6072  7.8129

