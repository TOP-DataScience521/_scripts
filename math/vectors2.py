from numpy import array


v = array([4, 5, 6])
w = array([10, 20, 30])

# >>> v + w
# array([14, 25, 36])


# >>> v + array([1, 2])
# ValueError: operands could not be broadcast together with shapes (3,) (2,)


x = array([[4], [5], [6]])
y = array([[10, 20, 30]])

# >>> x.shape
# (3, 1)
# >>>
# >>> y.shape
# (1, 3)


# >>> x + y
# array([[14, 24, 34],
#        [15, 25, 35],
#        [16, 26, 36]])


# >>> v + 5
# array([ 9, 10, 11])
# >>>
# >>> x + 5
# array([[ 9],
#        [10],
#        [11]])


# >>> v * 5
# array([20, 25, 30])
# >>>
# >>> x * 5
# array([[20],
#        [25],
#        [30]])

# >>> v * 0.1
# array([0.4, 0.5, 0.6])
# >>>
# >>> v / 10
# array([0.4, 0.5, 0.6])
# >>>
# >>> x * 0.1
# array([[0.4],
#        [0.5],
#        [0.6]])
# >>>
# >>> x / 10
# array([[0.4],
#        [0.5],
#        [0.6]])

