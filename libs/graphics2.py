from matplotlib import pyplot as plt
from numpy import arange, linspace


# точки графика функции f(x) = 2x
x1 = range(10)
f = range(0, 20, 2)

# точки графика дискретной функции g(x)
x2 = range(8)
g = [0, 4, 6, 2, 8, 5, 1, 3]

# точки графика функции p(x) = 0.3x²
x3 = arange(9)
p = 0.3 * x3**2

# точки графика функции q(x) = 0.3(x + 1)²
x4 = linspace(0, 9, 99, False)
q = 0.3 * (x4 + 1)**2

fig = plt.figure(figsize=(10, 6))
axs = fig.subplots()

axs.plot(x1, f, linewidth=5, label='f(x) = 2x')
axs.plot(x2, g, '.-', markersize=12, label='дискретная функция g(x)')
axs.plot(x3, p, '|-', linewidth=3, color='w', label='p(x) = 0.3x²')
axs.plot(x4, q, '|-', linewidth=3, color='#fff', label='q(x) = 0.3(x + 1)²')
axs.legend()

fig.show()

