from matplotlib import pyplot as plt
from numpy import array, loadtxt
from numpy.random import default_rng
from pandas import DataFrame

from pathlib import Path
from sys import path
from time import sleep

import _utils


points = loadtxt(Path(path[0]) / 'test_clusters-mixed.csv', delimiter=',')
x, y = points.T


# старт анимации
plt.ion()
speed = 10
fig = plt.figure(figsize=(9, 5))
axs = fig.subplots(1, 2)


# WCSS (within-clusters sum of squares) — сумма квадратов внутрикластерных расстояний
wcss_clusters = {}

# количество кластеров
for n in range(2, 10):
    # начальное положение центроид определяется случайной выборкой (без повторений) нужного количества значений зависимых переменных (координат)
    centroids = array(default_rng().choice(points, n, replace=False))
    
    # ==================== отрисовка кадра ====================
    axs[0].clear()
    axs[0].set(title='\nисходные данные\n')
    axs[0].scatter(x, y, s=10)
    fig.canvas.flush_events()
    sleep(2/speed)
    # ==================== отрисовка кадра ====================
    
    # ==================== отрисовка кадра ====================
    axs[0].clear()
    axs[0].set(title='\nначальное положение центроид\n')
    axs[0].scatter(x, y, s=10)
    axs[0].scatter(centroids.T[0], centroids.T[1], c='#ee1111', marker='v')
    fig.canvas.flush_events()
    sleep(5/speed)
    # ==================== отрисовка кадра ====================
    
    
    
    # общее количество итераций корректировок кластеров ограничено
    for j in range(15):
        
        # список порядковых номеров кластеров, позиционно совпадающий с points
        clusters = []
        # для каждой точки (вектора значений зависимой переменной)
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
        axs[0].clear()
        axs[0].set(title=f'цикл {j+1}\nкаждой точке сопоставляется кластер\nв зависимости от расстояния до центроид')
        for points_cluster_k in points_by_clusters:
            axs[0].scatter(*points_cluster_k.T, s=10)
        axs[0].scatter(centroids.T[0], centroids.T[1], c='#ee1111', marker='v')
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
        axs[0].clear()
        axs[0].set(title=f'цикл {j+1}\nновые координаты центроид вычисляются\nпо средним значениям координат сопоставленных точек')
        for points_cluster_k in points_by_clusters:
            axs[0].scatter(*points_cluster_k.T, s=10)
        axs[0].scatter(centroids_old.T[0], centroids_old.T[1], c='#ee1111', marker='v')
        axs[0].scatter(centroids.T[0], centroids.T[1], c='#ee111133', marker='v')
        fig.canvas.flush_events()
        sleep(2/speed)
        # ==================== отрисовка кадра ====================
        
        # ==================== отрисовка кадра ====================
        axs[0].clear()
        axs[0].set(title=f'цикл {j+1}\nкоординаты центроид смещаются\n')
        for points_cluster_k in points_by_clusters:
            axs[0].scatter(*points_cluster_k.T, s=10)
        axs[0].scatter(centroids.T[0], centroids.T[1], c='#ee1111', marker='v')
        fig.canvas.flush_events()
        sleep(2/speed)
        # ==================== отрисовка кадра ====================
    
    
    
    wcss = 0
    # для каждого кластера
    for points_cluster_k, centr_k in zip(points_by_clusters, centroids):
        centr_x_k, centr_y_k = centr_k
        # для каждой точки кластера
        for point_i in points_cluster_k:
            x_i, y_i = point_i
            # прибавить квадрат расстояния от точки до центроиды кластера
            # (математически эквивалентно _utils.euclid_dist(point_i, centr_k)**2)
            wcss += (x_i - centr_x_k)**2
            wcss += (y_i - centr_y_k)**2
    wcss_clusters[n] = wcss


    
    # ==================== отрисовка кадра ====================
    axs[1].clear()
    axs[1].set(
        title='\nсумма внутрикластерных расстояний\n',
        xticks=range(2, n+1),
    )
    axs[1].plot(wcss_clusters.keys(), wcss_clusters.values(), 'D-', c='#ee1111')
    fig.canvas.flush_events()
    sleep(5/speed)
    # ==================== отрисовка кадра ====================



plt.ioff()
plt.show()


# result = DataFrame({
#     'x': x,
#     'y': y,
#     'cluster': clusters
# })
# print(result)

