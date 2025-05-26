from pprint import pp
from random import uniform


class Monitor:
    def __init__(self, minimum, maximum):
        self.min = minimum
        self.max = maximum
    
    @staticmethod
    def info():
        print('значение находится в допустимом диапазоне')    
    
    @staticmethod
    def warning():
        print('значение находится за пределами допустимого диапазона')


# >>> pp(Monitor.__dict__)
# mappingproxy({'__module__': '__main__',
#               '__init__': <function Monitor.__init__ at 0x0000026885EE39C0>,
#               'info': <staticmethod(<function Monitor.info at 0x0000026885F2DEE0>)>,
#               'warning': <staticmethod(<function Monitor.warning at 0x0000026885F2DF80>)>,
#               '__dict__': <attribute '__dict__' of 'Monitor' objects>,
#               '__weakref__': <attribute '__weakref__' of 'Monitor' objects>,
#               '__doc__': None})

# >>> Monitor.info()
# значение находится в допустимом диапазоне
# >>>
# >>> Monitor.warning()
# значение находится за пределами допустимого диапазона

temp = Monitor(36.4, 36.9)

# >>> temp.info
# <function Monitor.info at 0x0000026885F2DEE0>
# >>>
# >>> temp.warning
# <function Monitor.warning at 0x0000026885F2DF80>

current_temp = uniform(36.5, 39.5)
if temp.min <= current_temp <= temp.max:
    temp.info()

# вызов статического метода от экземпляра не отличается от вызова функции от объекта класса:
# экземпляр.стат_метод(*позиционные, **ключевые) --> Класс.функция(*позиционные, **ключевые)

