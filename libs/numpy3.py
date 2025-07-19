from numpy import linspace, load, save, savez

from pathlib import Path
from pprint import pp
from sys import path


x1 = linspace(-10, 10, 21, dtype='int8')
x2 = linspace(-1, 1, 101)


script_dir = Path(path[0])

save(script_dir / 'numpy3_x1.npy', x1)

with open(script_dir / 'numpy3_x2.npy', 'wb') as fileout:
    save(fileout, x2)

with open(script_dir / 'numpy3_archive_pos.npz', 'wb') as fileout:
    savez(fileout, x1, x2)

savez(
    script_dir / 'numpy3_archive_keys.npz',
    graph1_X=x1,
    graph2_X=x2,
)


with open(script_dir / 'numpy3_x1.npy', 'rb') as filein:
    x1_ = load(filein)

x2_ = load(script_dir / 'numpy3_x2.npy')

x_archive1 = load(script_dir / 'numpy3_archive_pos.npz')

with open(script_dir / 'numpy3_archive_keys.npz', 'rb') as filein:
    x_archive2 = dict(load(filein))


# >>> type(x_archive1)
# <class 'numpy.lib.npyio.NpzFile'>
# >>>
# >>> print(*type(x_archive1).__mro__, sep='\n')
# <class 'numpy.lib.npyio.NpzFile'>
# <class 'collections.abc.Mapping'>
# <class 'collections.abc.Collection'>
# <class 'collections.abc.Sized'>
# <class 'collections.abc.Iterable'>
# <class 'collections.abc.Container'>
# <class 'object'>
# >>> 
# >>> 
# >>> x_archive1
# NpzFile 'C:\\Users\\Genndalf\\Documents\\Data Science\\521\\scripts\\libs\\numpy3_archive_pos.npz' with keys: arr_0, arr_1
# >>>
# >>> x_archive1.keys()
# KeysView(NpzFile 'C:\\Users\\Genndalf\\Documents\\Data Science\\521\\scripts\\libs\\numpy3_archive_pos.npz' with keys: arr_0, arr_1)
# >>>
# >>> list(x_archive1)
# ['arr_0', 'arr_1']
# >>>
# >>>
# >>> x_archive1['arr_0']
# array([-10,  -9,  -8,  -7,  -6,  -5,  -4,  -3,  -2,  -1,   0,   1,   2,
#          3,   4,   5,   6,   7,   8,   9,  10], dtype=int8)
# >>>
# >>> x_archive1['arr_1']
# array([-1.  , -0.98, -0.96, -0.94, -0.92, -0.9 , -0.88, -0.86, -0.84,
#        -0.82, -0.8 , -0.78, -0.76, -0.74, -0.72, -0.7 , -0.68, -0.66,
#        -0.64, -0.62, -0.6 , -0.58, -0.56, -0.54, -0.52, -0.5 , -0.48,
#        -0.46, -0.44, -0.42, -0.4 , -0.38, -0.36, -0.34, -0.32, -0.3 ,
#        -0.28, -0.26, -0.24, -0.22, -0.2 , -0.18, -0.16, -0.14, -0.12,
#        -0.1 , -0.08, -0.06, -0.04, -0.02,  0.  ,  0.02,  0.04,  0.06,
#         0.08,  0.1 ,  0.12,  0.14,  0.16,  0.18,  0.2 ,  0.22,  0.24,
#         0.26,  0.28,  0.3 ,  0.32,  0.34,  0.36,  0.38,  0.4 ,  0.42,
#         0.44,  0.46,  0.48,  0.5 ,  0.52,  0.54,  0.56,  0.58,  0.6 ,
#         0.62,  0.64,  0.66,  0.68,  0.7 ,  0.72,  0.74,  0.76,  0.78,
#         0.8 ,  0.82,  0.84,  0.86,  0.88,  0.9 ,  0.92,  0.94,  0.96,
#         0.98,  1.  ])
# >>>
# >>>
# >>> pp(x_archive2)
# {'graph1_X': array([-10,  -9,  -8,  -7,  -6,  -5,  -4,  -3,  -2,  -1,   0,   1,   2,
#          3,   4,   5,   6,   7,   8,   9,  10], dtype=int8),
#  'graph2_X': array([-1.  , -0.98, -0.96, -0.94, -0.92, -0.9 , -0.88, -0.86, -0.84,
#        -0.82, -0.8 , -0.78, -0.76, -0.74, -0.72, -0.7 , -0.68, -0.66,
#        -0.64, -0.62, -0.6 , -0.58, -0.56, -0.54, -0.52, -0.5 , -0.48,
#        -0.46, -0.44, -0.42, -0.4 , -0.38, -0.36, -0.34, -0.32, -0.3 ,
#        -0.28, -0.26, -0.24, -0.22, -0.2 , -0.18, -0.16, -0.14, -0.12,
#        -0.1 , -0.08, -0.06, -0.04, -0.02,  0.  ,  0.02,  0.04,  0.06,
#         0.08,  0.1 ,  0.12,  0.14,  0.16,  0.18,  0.2 ,  0.22,  0.24,
#         0.26,  0.28,  0.3 ,  0.32,  0.34,  0.36,  0.38,  0.4 ,  0.42,
#         0.44,  0.46,  0.48,  0.5 ,  0.52,  0.54,  0.56,  0.58,  0.6 ,
#         0.62,  0.64,  0.66,  0.68,  0.7 ,  0.72,  0.74,  0.76,  0.78,
#         0.8 ,  0.82,  0.84,  0.86,  0.88,  0.9 ,  0.92,  0.94,  0.96,
#         0.98,  1.  ])}


