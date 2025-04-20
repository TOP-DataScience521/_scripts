# def generator_func():
#     ...
#     yield ...
#     ...


def generator_func():
    print('начало выполнения')
    yield 12
    print('следующий шаг')
    yield 59
    print('следующий шаг')
    yield 41
    print('конец выполнения')


generator_obj = generator_func()

# >>> for elem in generator_obj:
# ...     print(elem)
# ... 
# начало выполнения
# 12
# следующий шаг
# 59
# следующий шаг
# 41
# конец выполнения


# >>> generator_obj.__next__()
# начало выполнения
# 12
# >>> generator_obj.__next__()
# следующий шаг
# 59
# >>> elem = generator_obj.__next__()
# следующий шаг
# >>> elem
# 41
# >>> generator_obj.__next__()
# конец выполнения
# StopIteration
# >>>
# >>> generator_obj.__next__()
# StopIteration
# >>>
# >>> for elem in generator_obj:
# ...     print(elem)
# ...
# >>>
# >>> list(generator_obj)
# []

