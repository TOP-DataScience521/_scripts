from math import exp


def step(x, cutoff=0):
    """Ступенчатая функция (Хэвисайда)."""
    if x < cutoff:
        return 0
    else:
        return 1


def linear(x, slope=1, intercept=0):
    """Линейная функция."""
    return x*slope + intercept


def relu(x, cutoff=0, slope=1):
    """Кусочно-линейная функция."""
    if x < cutoff:
        return 0
    else:
        return (x - cutoff)*slope


def lrelu(x, cutoff=0, slope=1, leak_slope=0.1):
    """Кусочно-линейная функция c "утечкой"."""
    if x < cutoff:
        return (x - cutoff)*leak_slope
    else:
        return (x - cutoff)*slope


def prelu(x, left=0, right=1):
    """Усечённая (параметризованная) кусочно-линейная функция с нормализацией."""
    if x < left:
        return 0
    elif x > right:
        return 1
    else:
        slope = 1 / (right - left)
        return (x - left)*slope


def sigmoid(x, a=1, b=0):
    """Сигмоидальная (логистическая) функция с нормализацией."""
    return 1 / (1 + exp(-a*x - b))


def tanh(x, a=1, b=0):
    """Функция гиперболического тангенса."""
    return (exp(a*x + b) - exp(-a*x - b)) / (exp(a*x + b) + exp(-a*x - b))



if __name__ == '__main__':
    
    from matplotlib import pyplot as plt
    from numpy import linspace
    
    from json import loads
    from pathlib import Path
    from sys import path
    
    script_dir = Path(path[0])
    test_params_path = script_dir / 'activations_test_params.json'
    figures_dir = script_dir / 'activations test'
    
    funcs = (step, linear, relu, lrelu, prelu, sigmoid, tanh)
    funcs_params = loads(test_params_path.read_text(encoding='utf-8'))
    axes_params = (
        {'xlim': (-5.1, 5.1), 'ylim': (-0.1, 1.1)},  # step
        {'xlim': (-2.1, 2.1), 'ylim': (-2.1, 2.1)},  # linear
        {'xlim': (-1.1, 3.1), 'ylim': (-2.1, 2.1)},  # relu
        {'xlim': (-5.1, 5.1), 'ylim': (-5.1, 5.1)},  # lrelu
        {'xlim': (-3.1, 3.1), 'ylim': (-0.1, 1.1)},  # prelu
        {'xlim': (-15.1, 15.1), 'ylim': (-0.1, 1.1)},  # sigmoid
        {'xlim': (-15.1, 15.1), 'ylim': (-1.1, 1.1)},  # tanh
    )
    
    for func, func_params, axs_params in zip(funcs, funcs_params, axes_params):
        n = len(func_params)
        r, c = sum(divmod(n, 2)), 2
        
        fig = plt.figure(figsize=(c*5, r*5))
        axs = fig.subplots(r, c)
        
        for i in range(n):
            i_a = divmod(i, 2) if n > 2 else i
            
            x = linspace(*axs_params['xlim'], 500)
            y = []
            for _ in x:
                y.append(func(_, **func_params[i]))
            
            kwdefaults = dict(zip(func.__code__.co_varnames[1:], func.__defaults__))
            title = ', '.join(
                f'{name}={val}'
                for name, val in (kwdefaults | func_params[i]).items()
            )
            
            # вариант со вспомогательными ортогональными линиями через (0;0)
            axs[i_a].axhline(color='#f8f8f2', lw=0.5, alpha=0.5)
            axs[i_a].axvline(color='#f8f8f2', lw=0.5, alpha=0.5)
            
            # вариант с осями через (0;0)
            # axs[i_a].spines['top'].set_visible(False)
            # axs[i_a].spines['right'].set_visible(False)
            # axs[i_a].spines['bottom'].set_position('zero')
            # axs[i_a].spines['left'].set_position('zero')
            
            axs[i_a].plot(x, y, color='C1', lw=2.5)
            axs[i_a].set(**axs_params, title=title)
        
        fig.savefig(figures_dir / f'{func.__name__}.png')


