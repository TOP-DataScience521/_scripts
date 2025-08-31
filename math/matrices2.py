from numpy import array, dot, empty, full

import matrices1 as data


# >>> data.matrix1 + data.matrix2
# array([[ 2, 11,  5,  9, -1],
#        [-4,  3,  8,  6,  5],
#        [ 5,  4, 10,  0,  1]])
# >>>
# >>> data.matrix1 - data.matrix2
# array([[ 0,  9,  3,  7, -3],
#        [-6,  1,  6,  4,  3],
#        [ 3,  2,  8, -2, -1]])


# транслирование: на основе скаляра 4 создаётся матрица размерностью 3x5 (размерность data.matrix2), далее осуществляется обычное поэлементное сложение
# >>> data.matrix2 + 4
# array([[5, 5, 5, 5, 5],
#        [5, 5, 5, 5, 5],
#        [5, 5, 5, 5, 5]])


# >>> data.matrix2 * 5
# array([[5, 5, 5, 5, 5],
#        [5, 5, 5, 5, 5],
#        [5, 5, 5, 5, 5]])
# >>>
# >>> data.matrix6 * 9
# array([[9, 0, 0, 0],
#        [0, 9, 0, 0],
#        [0, 0, 9, 0],
#        [0, 0, 0, 9]])


# >>> data.matrix4 * data.matrix4
# array([[1, 4],
#        [4, 0],
#        [1, 4]])
# >>>
# >>> data.matrix4 * full(shape=(3, 2), fill_value=10)
# array([[-10, -20],
#        [ 20,   0],
#        [ 10, -20]])


m7 = array([
    [2, 4, 6],
    [1, 3, 5],
])
m8 = array([
    [-1, 2, 0, 1],
    [-1, 2, 0, 1],
    [-1, 2, 0, 1],
])

m_78_1 = array([
    
    [sum(m7[0]*m8[:,0]),  sum(m7[0]*m8[:,1]),  sum(m7[0]*m8[:,2]),  sum(m7[0]*m8[:,3])],
    
    [sum(m7[1]*m8[:,0]),  sum(m7[1]*m8[:,1]),  sum(m7[1]*m8[:,2]),  sum(m7[1]*m8[:,3])],
])

m_78_2 = empty(shape=(m7.shape[0], m8.shape[1]), dtype=int)
for i in range(m7.shape[0]):
    for j in range(m8.shape[1]):
        m_78_2[i,j] = dot(m7[i], m8[:,j])

m_78_3 = m7 @ m8

# >>> m_78_1
# array([[-12,  24,   0,  12],
#        [ -9,  18,   0,   9]])

# >>> m_78_1 == m_78_2
# array([[ True,  True,  True,  True],
#        [ True,  True,  True,  True]])
# >>>
# >>> (m_78_1 == m_78_2).all()
# np.True_
# >>>
# >>> m_78_2 == m_78_3
# array([[ True,  True,  True,  True],
#        [ True,  True,  True,  True]])
# >>>
# >>> (m_78_2 == m_78_3).all()
# np.True_


# умножение матриц некоммутативно
# >>> m8 @ m7
# ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0, with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 2 is different from 4)

