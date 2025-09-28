from matplotlib import pyplot as plt
from matplotlib import rcParams
from numpy import array, concatenate, corrcoef, linspace
from numpy.random import default_rng

from itertools import combinations
from math import ceil


rcParams['toolbar'] = 'None'
rcParams['lines.markersize'] = 3


class GraphCorrAnalysis:
    graph_params = rcParams
    
    def __init__(self, var1, var2, *variables):
        self.data = array([var1, var2, *variables])
        self.combs = array(list(combinations(self.data, 2)))
    
    def __repr__(self):
        return f'<GraphCorrAnalysis: {len(self.data)} variables, {len(self.combs)} combinations>'
    
    def _grid(self):
        n = len(self.combs)
        x_, y_, diff = 1, 1, float('inf')
        for x in range(1, n+1):
            for y in range(1, n+1):
                if x * y == n:
                    if abs(x - y) < diff:
                        x_, y_, diff = x, y, abs(x - y)
        return x_, y_
    
    def draw(self):
        x, y = self._grid()
        fig = plt.figure(figsize=(6, 6), dpi=120, layout='constrained')
        axs = fig.subplots(x, y, squeeze=False)
        for i in range(x):
            for j in range(y):
                var1, var2 = self.combs[i*y + j]
                corr_coef = corrcoef(var1, var2)[0,1]
                axs[i,j].scatter(var1, var2)
                axs[i,j].set(
                    xticks=[],
                    yticks=[],
                    title=f'r = {corr_coef:.2f}'
                )
        fig.show()


N = 150

var1 = linspace(1, N, N)

var2 = default_rng().normal(scale=2, size=N)

var3 = 0.001 * var1**2 
var3 = concatenate([
    var3[:N//4] * abs(default_rng().normal(loc=1, scale=2.5, size=N//4)),
    var3[N//4:] * abs(default_rng().normal(loc=1, scale=0.25, size=N-N//4)),
])

var4 = concatenate([var1[:N//2]*0.15, var1[N//2:]*-0.15 + 23])
var4 = var4 * default_rng().normal(loc=1, scale=0.1, size=N)


gca = GraphCorrAnalysis(var1, var2, var3, var4)
gca.draw()

