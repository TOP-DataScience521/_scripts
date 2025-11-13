from matplotlib import pyplot as plt
from numpy import array, loadtxt
from pandas import DataFrame

from pathlib import Path
from random import uniform
from sys import path
from time import sleep

import _utils


points = loadtxt(Path(path[0]) / 'test_clusters.csv', delimiter=',')
x, y = points.T


# старт анимации
plt.ion()
speed = 2
fig = plt.figure(figsize=(5, 5))
axs = fig.subplots()

# ==================== отрисовка кадра ====================
axs.clear()
axs.set(title='\nисходные данные\n')
axs.scatter(x, y, s=10)
fig.canvas.flush_events()
sleep(3/speed)
# ==================== отрисовка кадра ====================



# начальное положение центроид определяется на границах диапазонов значений зависимых переменных (координат)
# centroids = array([
#     (x.min(), y.min()),
#     (x.min(), y.max()),
#     (x.max(), y.max()),
# ])

# начальное положение центроид определяется случайным образом в диапазонах значений зависимых переменных (координат)
centroids = array([
    (uniform(x.min(), x.max()), uniform(y.min(), y.max())),
    (uniform(x.min(), x.max()), uniform(y.min(), y.max())),
    (uniform(x.min(), x.max()), uniform(y.min(), y.max())),
])
# количество кластеров
n = len(centroids)


# ==================== отрисовка кадра ====================
axs.clear()
axs.set(title='\nначальное положение центроид\n')
axs.scatter(x, y, s=10)
axs.scatter(centroids.T[0], centroids.T[1], c='#ee1111', marker='v')
fig.canvas.flush_events()
sleep(5/speed)
# ==================== отрисовка кадра ====================


# общее количество итераций корректировок кластеров ограничено
for j in range(7):


    # список порядковых номеров кластеров, позиционно совпадающий с points
    clusters = []
    # для каждой точки
    for point_i in points:
        distances = []
        # до каждой центроиды
        for centr_k in centroids:
            # вычисляется расстояние
            distances.append(_utils.euclid_dist(point_i, centr_k))
        # из расстояний до каждой центроиды выбирается минимальное
        # индекс расстояния — это порядковый номер кластера
        clusters.append(array(distances).argmin())
    
    clusters = array(clusters)
    # группировка значений зависмых переменных по кластерам
    points_by_clusters = [
        points[clusters == k]
        for k in range(n)
    ]
    
    
    # ==================== отрисовка кадра ====================
    axs.clear()
    axs.set(title=f'цикл {j+1}\nкаждой точке сопоставляется кластер\nв зависимости от расстояния до центроид')
    for points_cluster_k in points_by_clusters:
        axs.scatter(*points_cluster_k.T, s=10)
    axs.scatter(centroids.T[0], centroids.T[1], c='#ee1111', marker='v')
    fig.canvas.flush_events()
    sleep(3/speed)
    # ==================== отрисовка кадра ====================
    
    
    
    # смещение координат центроид
    centroids_old = centroids.copy()
    centroids = []
    for points_cluster_k in points_by_clusters:
        x_k, y_k = points_cluster_k.T
        # новые координаты центроиды вычисляются как средние значения соответствующих координат точек, ранее отнесённых к этой центроиде
        centroids.append((x_k.mean(), y_k.mean()))
    centroids = array(centroids)
    
    
    
    # ==================== отрисовка кадра ====================
    axs.clear()
    axs.set(title=f'цикл {j+1}\nновые координаты центроид вычисляются\nпо средним значениям координат сопоставленных точек')
    for points_cluster_k in points_by_clusters:
        axs.scatter(*points_cluster_k.T, s=10)
    axs.scatter(centroids_old.T[0], centroids_old.T[1], c='#ee1111', marker='v')
    axs.scatter(centroids.T[0], centroids.T[1], c='#ee111133', marker='v')
    fig.canvas.flush_events()
    sleep(2/speed)
    # ==================== отрисовка кадра ====================
    
    # ==================== отрисовка кадра ====================
    axs.clear()
    axs.set(title=f'цикл {j+1}\nкоординаты центроид смещаются\n')
    for points_cluster_k in points_by_clusters:
        axs.scatter(*points_cluster_k.T, s=10)
    axs.scatter(centroids.T[0], centroids.T[1], c='#ee1111', marker='v')
    fig.canvas.flush_events()
    sleep(2/speed)
    # ==================== отрисовка кадра ====================



plt.ioff()
plt.show()


result = DataFrame({
    'x': x,
    'y': y,
    'cluster': clusters
})
print(result)

