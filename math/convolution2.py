from numpy import array, zeros
from matplotlib import pyplot as plt
from scipy.signal import convolve


image = zeros(shape=(100,100))
image[:,20:30] = 255
image[:,60:80] = 255
image[70:,50:] = 0

# в качестве ядра свёртки используется модифицированный фильтр Прюитта
filter_vert = array([
    [1, 0, -1],
    [2, 0, -2],
    [1, 0, -1],
])

conv_matr = convolve(image, filter_vert, mode='valid')


fig = plt.figure(figsize=(10,5))
axs = fig.subplots(1, 2)

axs[0].imshow(image, cmap='gray')
axs[1].imshow(conv_matr.round(0), cmap='gray')

fig.show()

