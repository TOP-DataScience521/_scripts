from numpy import array, fromiter, ndarray, ones

from typing import Callable, Union


array_like = Union[list, tuple, ndarray]


class Neuron:
    """
    Модель искусственного нейрона с динамическим количеством входов.
    """
    def __init__(self, activation_func: Callable, **activation_func_params):
        self._non_linear = activation_func
        self._af_params = activation_func_params
        self.weights: ndarray = None
    
    @property
    def in_count(self):
        if self.weights is None:
            return 0
        else:
            return len(self.weights)
    
    def _linear(self, x: array_like):
        if self.weights is None:
            self.weights = ones(shape=x.shape)
        return (x * self.weights).sum()
    
    def out(self, x: array_like):
        return self._non_linear(
            self._linear(x),
            **self._af_params
        )


class DenseLayer:
    """
    Модель полносвязного слоя искусственных нейронов.
    """
    def __init__(self, n: int, activation_func: Callable, **activation_func_params):
        neurons = []
        for _ in range(n):
            neurons.append(Neuron(
                activation_func,
                **activation_func_params
            ))
        self.neurons: ndarray = array(neurons)
    
    def out(self, x: array_like):
        return fromiter((neuron.out(x) for neuron in self.neurons), float)


