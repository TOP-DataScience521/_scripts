from matplotlib import pyplot as plt
from numpy import array, diag, eye, ones, zeros
from numpy.random import default_rng


# прямоугольная матрица псевдо-случайных чисел
matrix1 = array([
    [1, 10, 4, 8, -2],
    [-5, 2, 7, 5, 4],
    [4, 3, 9, -1, 0],
])
# >>> matrix1
# array([[ 1, 10,  4,  8, -2],
#        [-5,  2,  7,  5,  4],
#        [ 4,  3,  9, -1,  0]])

# прямоугольная матрица единиц
matrix2 = ones(shape=matrix1.shape, dtype=int)
# >>> matrix2
# array([[1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1]])

# прямоугольная нулевая матрица
matrix3 = zeros(shape=(3, 2), dtype=int)
# >>> matrix3
# array([[0, 0],
#        [0, 0],
#        [0, 0]])

generator = default_rng()
# прямоугольная матрица псевдо-случайных чисел
matrix4 = generator.uniform(-5, 5, size=(3, 2)).astype(dtype=int)
# >>> matrix4
# array([[1, 0],
#        [4, 2],
#        [0, 2]])

# диагональная матрица
matrix5 = diag([3, 0, -2, 5])
# >>> matrix5
# array([[ 3,  0,  0,  0],
#        [ 0,  0,  0,  0],
#        [ 0,  0, -2,  0],
#        [ 0,  0,  0,  5]])

# единичная матрица (всегда квадратная)
matrix6 = eye(4, dtype=int)
# >>> matrix6
# array([[1, 0, 0, 0],
#        [0, 1, 0, 0],
#        [0, 0, 1, 0],
#        [0, 0, 0, 1]])


if __name__ == '__main__':
    
    fig = plt.figure(figsize=(6, 10))
    axs = fig.subplots(3, 2)
    
    axs[0, 0].matshow(matrix1)
    axs[0, 1].matshow(matrix2)
    
    axs[1, 0].matshow(matrix3, cmap='gray')
    axs[1, 1].matshow(matrix4, cmap='gray')
    
    axs[2, 0].imshow(matrix5, cmap='gray')
    axs[2, 1].imshow(matrix6, cmap='gray')
    
    fig.show()

