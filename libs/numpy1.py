from numpy import empty, full, ones, zeros


arr1 = empty(shape=5)
arr2 = empty(shape=(10, 20, 3))

# >>> type(arr1)
# <class 'numpy.ndarray'>
# >>>
# >>> type(arr2)
# <class 'numpy.ndarray'>
# >>>
# >>>
# >>> arr1.shape
# (5,)
# >>>
# >>> arr2.shape
# (10, 20, 3)

arr3 = zeros(shape=6)
arr4 = zeros(shape=(2, 7))

# >>> arr3
# array([0., 0., 0., 0., 0., 0.])
# >>>
# >>> arr4
# array([[0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0.]])
# >>>
# >>>
# >>> print(arr3)
# [0. 0. 0. 0. 0. 0.]
# >>>
# >>> print(arr4)
# [[0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0.]]

arr5 = ones(shape=(2, 3, 4, 2))

# >>> arr5
# array([[[[1., 1.],
#          [1., 1.],
#          [1., 1.],
#          [1., 1.]],
#         
#         [[1., 1.],
#          [1., 1.],
#          [1., 1.],
#          [1., 1.]],
#         
#         [[1., 1.],
#          [1., 1.],
#          [1., 1.],
#          [1., 1.]]],
#         
#         
#        [[[1., 1.],
#          [1., 1.],
#          [1., 1.],
#          [1., 1.]],
#         
#         [[1., 1.],
#          [1., 1.],
#          [1., 1.],
#          [1., 1.]],
#         
#         [[1., 1.],
#          [1., 1.],
#          [1., 1.],
#          [1., 1.]]]])

arr6 = full(shape=(3, 3), fill_value=9)
arr7 = full(shape=5, fill_value='empty')
arr8 = full(10, True)

# >>> arr6
# array([[9, 9, 9],
#        [9, 9, 9],
#        [9, 9, 9]])
# >>>
# >>> arr7
# array(['empty', 'empty', 'empty', 'empty', 'empty'], dtype='<U5')
# >>> print(arr8)
# [ True  True  True  True  True  True  True  True  True  True]


# >>> arr3[0]
# np.float64(0.0)
# >>>
# >>> type(arr3[0])
# <class 'numpy.float64'>
# >>>
# >>>
# >>> arr5[0][0][0][0]
# np.float64(1.0)
# >>>
# >>> arr5[0, 0, 0, 0]
# np.float64(1.0)
# >>> 
# >>> type(arr5[0, 0, 0, 0])
# <class 'numpy.float64'>
# >>>
# >>>
# >>> arr6[0, 0]
# np.int64(9)
# >>>
# >>> type(arr6[0, 0])
# <class 'numpy.int64'>
# >>>
# >>>
# >>> arr7[0]
# np.str_('empty')
# >>>
# >>> type(arr7[0])
# <class 'numpy.str_'>
# >>>
# >>>
# >>> arr8[0]
# np.True_
# >>>
# >>> type(arr8[0])
# <class 'numpy.bool'>


# >>> zeros((5, 5), dtype='int8')
# array([[0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0]], dtype=int8)
# >>>
# >>> zeros((5, 5), dtype='int16')
# array([[0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0]], dtype=int16)
# >>>
# >>> zeros((5, 5), dtype='int64')
# array([[0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0]])
# >>>
# >>> full((4, 4), 0.01, dtype='float32')
# array([[0.01, 0.01, 0.01, 0.01],
#        [0.01, 0.01, 0.01, 0.01],
#        [0.01, 0.01, 0.01, 0.01],
#        [0.01, 0.01, 0.01, 0.01]], dtype=float32)
# >>>
# >>>
# >>> full(shape=5, fill_value=325, dtype='int8')
# array([69, 69, 69, 69, 69], dtype=int8)
# >>>
# >>> full(shape=5, fill_value=325, dtype='int16')
# array([325, 325, 325, 325, 325], dtype=int16)
# >>>
# >>> 325 - 256
# 69
# >>>
# >>> full(shape=5, fill_value=10**100, dtype='int64')
# OverflowError: int too big to convert

