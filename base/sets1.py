numbers = {1, 5, -3, 9, 2}

# >>> numbers
# {1, 2, 5, 9, -3}
# >>>
# >>> type(numbers)
# <class 'set'>
# >>>
# >>> len(numbers)
# 5

for elem in numbers:
    print(elem)

# 1
# 2
# 5
# 9
# -3


text = 'A set object is an unordered collection of distinct hashable objects'

# >>> len(text)
# 68
# >>> set(text)
# {'t', 's', 'a', 'd', 'r', 'i', 'u', ' ', 'j', 'b', 'c', 'l', 'h', 'A', 'o', 'n', 'e', 'f'}
# >>>
# >>> len(set(text))
# 18


items = ['1', 1, 'a', 'а', 0, 0, False, None]

# >>> len(items)
# 8
# >>> set(items)
# {0, 1, None, 'a', 'а', '1'}
# >>>
# >>> len(set(items))
# 6


key = {1, 3, 5, 1, 2, 3}

# >>> type(key)
# <class 'set'>
# >>>
# >>> {key: 'множество'}
# TypeError: unhashable type: 'set'


key = frozenset({1, 3, 5, 1, 2, 3})

# >>> type(key)
# <class 'frozenset'>
# >>>
# >>> {key: 'множество'}
# {frozenset({1, 2, 3, 5}): 'множество'}

