from numpy import array
from scipy.signal import convolve


f = [2, 3, 9, 1, 6, 8]
g = [3, 2, 1]

#               [3 2 1]
#     [8 6 1 9 3 2]0 0
#     
#             [3 2 1]
#     [8 6 1 9 3 2]0
#     
#           [3 2 1]
#     [8 6 1 9 3 2]
#     
#         [3 2 1]
#     [8 6 1 9 3 2]
#     
#       [3 2 1]
#     [8 6 1 9 3 2]
#     
#     [3 2 1]
#     [8 6 1 9 3 2]
# 
#   [3 2 1]
#    0[8 6 1 9 3 2]
# 
# [3 2 1]
#  0 0[8 6 1 9 3 2]

n = len(g)
f_ = [0]*(n-1) + f[::-1] + [0]*(n-1)
conv = []
for i in range(len(f)-1+n-1, -1, -1):
    window = array(f_[i:i+n])
    kernel = array(g)
    print(window, '*', kernel)
    conv.append(sum(window * kernel))

print('\n', array(conv), sep='')
print('\n', convolve(f, g), sep='')

