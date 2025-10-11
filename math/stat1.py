__all__ = [
    'sample',
    'X',
    'm',
    'W',
    'X_intervals',
    'm_intervals',
    'X_intervals_means',
]


from numpy import array, count_nonzero, sort, where

from random import randint


# генеральная совокупность определена в интервале (a; b)
a = 10
b = 20


# объём выборочной совокупности
n = 30
# выборочная совокупность (выборка)
sample = [randint(a, b) for _ in range(n)]

# >>> sample
# [16, 20, 13, 15, 14, 19, 18, 17, 10, 16, 10, 18, 20, 13, 11, 18, 13, 12, 16, 19, 13, 11, 20, 12, 10, 18, 18, 10, 14, 18]

# >>> sorted(sample)
# [10, 10, 10, 10, 11, 11, 12, 12, 13, 13, 13, 13, 14, 14, 15, 16, 16, 16, 17, 18, 18, 18, 18, 18, 18, 19, 19, 20, 20, 20]


# переход от выборочной совокупности к дискретному статистическому ряду
X = array(sorted(set(sample)))
m = array([sample.count(elem) for elem in X])
W = m / n

# дискретный статистический ряд
# >>> print(array([X, m]))
# [[10 11 12 13 14 15 16 17 18 19 20]
#  [ 4  2  2  4  2  1  3  1  6  2  3]]


# переход от дискретного статистического ряда к выборочной совокупности
sample_ = array([
    X[i]
    for i in range(len(X))
        for _ in range(m[i])
])


# переход от дискретного статистического ряда к интервальному статистическому ряду
X_intervals = [(10, 12), (12, 14), (14, 16), (16, 18), (18, 20)]

def sample_to_interval(sample, intervals):
    sample = list(sample)
    X = array(sorted(set(sample)))
    M = [sample.count(elem) for elem in X]
    
    m_intervals = []
    # для первого интервала
    x1, x2 = intervals[0]
    m_total = 0
    for x in X:
        i = where(X == x)[0][0]
        if x1 <= x < x2:
            m_total += M[i]
        elif x == x2:
            m_total += sum(divmod(M[i], 2))
    m_intervals.append(m_total)
    # для промежуточных интервалов
    for x1, x2 in intervals[1:-1]:
        m_total = 0
        for x in X:
            i = where(X == x)[0][0]
            if x == x1:
                m_total += divmod(M[i], 2)[0]
            elif x1 < x < x2:
                m_total += M[i]
            elif x == x2:
                m_total += sum(divmod(M[i], 2))
        m_intervals.append(m_total)
    # для последнего интервала
    x1, x2 = intervals[-1]
    m_total = 0
    for x in X:
        i = where(X == x)[0][0]
        if x == x1:
            m_total += divmod(M[i], 2)[0]
        elif x1 < x <= x2:
            m_total += M[i]
    m_intervals.append(m_total)
    return m_intervals


m_intervals = sample_to_interval(sample, X_intervals)

# переход от интервального статистического ряда к дискретному статистическому ряду со средними значениями интервалов
X_intervals_means = [sum(interval)/2 for interval in X_intervals]

# >>> print(array([X_intervals_means, m_intervals]))
# [[11. 13. 15. 17. 19.]
#  [ 7.  6.  4.  5.  8.]]

