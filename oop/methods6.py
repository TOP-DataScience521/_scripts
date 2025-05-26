from pprint import pp


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @classmethod
    def square(cls, size):
        return cls(size, size)


# вызов классового метода от объекта класса и от объекта экземпляра приводят к одной подмене вызова
# Класс.класс_метод(*позиционные, **ключевые) --> Класс.функция(Класс, *позиционные, **ключевые)
# экземпляр.класс_метод(*позиционные, **ключевые) --> Класс.функция(Класс, *позиционные, **ключевые)


# >>> Rectangle.square
# <bound method Rectangle.square of <class '__main__.Rectangle'>>
# >>>
# >>> sq1 = Rectangle.square(5)
# >>> sq1
# <__main__.Rectangle object at 0x000001F4572A9250>
# >>>
# >>> sq1.__dict__
# {'width': 5, 'height': 5}
# >>>
# >>>
# >>> sq1.square
# <bound method Rectangle.square of <class '__main__.Rectangle'>>
# >>>
# >>> sq2 = sq1.square(10)
# >>> sq2
# <__main__.Rectangle object at 0x000001F4572AB380>
# >>>
# >>> sq2.__dict__
# {'width': 10, 'height': 10}

