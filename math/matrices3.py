from matplotlib import pyplot as plt
from numpy import array, concat, zeros


n = 200

m_00 = zeros(shape=(n, n, 3), dtype=int)
m_01 = zeros(shape=(n, n, 3), dtype=int)
m_10 = zeros(shape=(n, n, 3), dtype=int)
m_11 = zeros(shape=(n, n, 3), dtype=int)

for i in range(n):
    for j in range(n):
        m_00[i,j,0] = 255
        m_01[i,j,1] = 255
        m_10[i,j,2] = 255
        m_11[i,j,0] = 255
        m_11[i,j,1] = 255
        m_11[i,j,2] = 255


img = concat(
    [
        concat([m_00, m_01], axis=1),
        concat([m_10, m_11], axis=1),
    ],
    axis=0
)


fig = plt.figure(figsize=(5, 5))
axs = fig.subplots()

axs.imshow(img)

fig.show()

