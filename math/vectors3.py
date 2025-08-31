from numpy import array, dot
from numpy.linalg import norm


v1 = array([2, 4, 5])

# модуль вектора = норма вектора = геометрическая длина вектора
v1_module = sum([num**2 for num in v1])**0.5

# >>> v1_module
# np.float64(6.708203932499369)
# >>>
# >>> v1_module == norm(v1)
# np.True_


# норммированный вектор
# >>> v1 / norm(v1)
# array([0.2981424 , 0.59628479, 0.74535599])
# >>>
# >>> norm(v1 / norm(v1))
# np.float64(1.0)


a = array([1, 2, 3, 4])
b = array([5, 6, 7, 8])

# внутреннее (точечное, векторное) произведение
ab_dot = sum([a[i]*b[i] for i in range(a.shape[0])])

# результат — скаляр
# >>> ab_dot
# np.int64(70)
# >>>
# >>> ab_dot == dot(a, b)
# np.True_


# поэлементное (адамарово) произведение
# результат — вектор
# >>> a * b
# array([ 5, 12, 21, 32])
# >>>
# >>> a * array([5, 6])
# ValueError: operands could not be broadcast together with shapes (4,) (2,)


# внешнее произведение — для ориентированных векторов
# результат — матрица
# >>> array([[1], [2], [3], [4]]) * array([[5, 6]])
# array([[ 5,  6],
#        [10, 12],
#        [15, 18],
#        [20, 24]])

