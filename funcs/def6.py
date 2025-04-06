def product(*numbers, start=1):
    print(type(numbers), numbers, sep='\n')
    for num in numbers:
        start = start * num
    return start


# >>> product(5)
# <class 'tuple'>
# (5,)
# 5
# >>>
# >>> product(5, 2)
# <class 'tuple'>
# (5, 2)
# 10
# >>>
# >>> product(5, 2, 9)
# <class 'tuple'>
# (5, 2, 9)
# 90


# >>> nums = range(2, 10)
# >>> product(*nums)
# <class 'tuple'>
# (2, 3, 4, 5, 6, 7, 8, 9)
# 362880

