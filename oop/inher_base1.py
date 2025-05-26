class ExcessElementsError(Exception):
    pass


class FixedList(list):
    def __init__(self, max_elements):
        self.limit = max_elements
    
    def append(self, element):
        if len(self) < self.limit:
            super().append(element)
        else:
            raise ExcessElementsError
    
    def extend(self, iterable):
        if len(self) < self.limit:
            iterable = list(iterable)
            if len(self) + len(iterable) < self.limit:
                super().extend(iterable)
            else:
                for i in range(self.limit - len(self)):
                    super().append(iterable[i])
        else:
            raise ExcessElementsError


# >>> FixedList.__mro__
# (<class '__main__.FixedList'>, <class 'list'>, <class 'object'>)

log = FixedList(5)

# >>> log.append('первая запись')
# >>> log
# ['первая запись']
# >>>
# >>> log.append('вторая запись')
# >>> log.append('третья запись')
# >>> log.append('четвёртая запись')
# >>> log.append('пятая запись')
# >>> log
# ['первая запись', 'вторая запись', 'третья запись', 'четвёртая запись', 'пятая запись']
# >>>
# >>> log.append('шестая запись')
# ExcessElementsError
# >>>
# >>> try:
# ...     log.append('шестая запись')
# ... except ExcessElementsError:
# ...     print(f'превышено количество элементов ({log.limit}) списка')
# ...
# превышено количество элементов (5) списка

