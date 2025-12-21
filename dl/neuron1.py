class Neuron:
    """
    Модель искусственного нейрона с фиксированым количеством входов и фиксированной функцией активации (ступенчатая).
    """
    def __init__(self, weight1=1, weight2=1):
        self.weight1 = weight1
        self.weight2 = weight2
    
    def _linear(self, x1, x2):
        """Линейное преобразование — сумматор."""
        return x1*self.weight1 + x2*self.weight2
    
    def _non_linear(self, x):
        """Нелинейное преобразование — ступенчатая функция (Хэвисайда)."""
        if x < 0:
            return 0
        else:
            return 1
    
    def out(self, x1, x2):
        return self._non_linear(self._linear(x1, x2))


temperature1 = (9, 10)
temperature2 = (10, 16)
temperature3 = (8, -5)

# подбор весов
weather = Neuron(-1, 1)

print(
    weather.out(*temperature1),
    weather.out(*temperature2),
    weather.out(*temperature3),
)

