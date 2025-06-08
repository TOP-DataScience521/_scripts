# >>> dict_of_ranges = {
# ...     (1, 10): 'первый диапазон',
# ...     (11, 20): 'второй диапазон',
# ...     (21, 30): 'третий диапазон',
# ... }
# >>> dict_of_ranges[5]
# 'первый диапазон'
# >>> dict_of_ranges[(1, 10)]
# 'первый диапазон'

from collections.abc import Iterable
from numbers import Number


class DictOfRanges(dict):
    # @staticmethod
    # def __check_key(key):
    #     if isinstance(key, Iterable):
    #         if len(key) == 2:
    #             left, right = key
    #             if isinstance(left, Number) and isinstance(right, Number):
    #                 if left < right:
    #                     return True
    #     return False
    
    @staticmethod
    def __check_key(key):
        try:
            left, right = key
        except (TypeError, ValueError):
            return False
        else:
            if isinstance(left, Number) and isinstance(right, Number):
                if left < right:
                    return True
            return False
    
    def __getitem__(self, key):
        if isinstance(key, Number):
            for left, right in self:
                if left <= key <= right:
                    return super().__getitem__((left, right))
            raise KeyError
        elif self.__check_key(key):
            return super().__getitem__(key)
        else:
            raise TypeError


dict_of_ranges = DictOfRanges({
    (1, 10): 'первый диапазон',
    (11, 20): 'второй диапазон',
    (21, 30): 'третий диапазон',
})

# >>> dict_of_ranges
# {(1, 10): 'первый диапазон', (11, 20): 'второй диапазон', (21, 30): 'третий диапазон'}
# >>>
# >>> type(dict_of_ranges)
# <class '__main__.DictOfRanges'>
# >>>
# >>>
# >>> dict_of_ranges[(1, 10)]
# 'первый диапазон'
# >>>
# >>> dict_of_ranges[5]
# 'первый диапазон'
# >>>
# >>> dict_of_ranges[15]
# 'второй диапазон'
# >>>
# >>> dict_of_ranges[50]
# KeyError

