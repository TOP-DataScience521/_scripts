# класс предок / родительский класс / базовый класс / надкласс
class A:
    attr1 = 123
    attr2 = 'abc'


# класс потомок / дочерний класс / производный класс / подкласс
class B(A):
    pass


from pprint import pp

# цепочки наследования
# >>> A.__mro__
# (<class '__main__.A'>, <class 'object'>)
# >>>
# >>> B.__mro__
# (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)


# >>> pp(A.__dict__)
# mappingproxy({'__module__': '__main__',
#               'attr1': 123,
#               'attr2': 'abc',
#               '__dict__': <attribute '__dict__' of 'A' objects>,
#               '__weakref__': <attribute '__weakref__' of 'A' objects>,
#               '__doc__': None})
# >>>
# >>> pp(B.__dict__)
# mappingproxy({'__module__': '__main__', '__doc__': None})


# расширение области видимости по цепочке наследования
# >>> B.attr1
# 123
# >>> B.attr2
# 'abc'

# >>> b = B()
# >>>
# >>> b.__dict__
# {}
# >>> b.attr1
# 123
# >>> b.attr2
# 'abc'

