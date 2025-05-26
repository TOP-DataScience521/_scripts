class Table:
    width = 0
    depth = 0
    height = 0
    legs = 0


# объект класса
# >>> Table
# <class '__main__.Table'>

# внутреннее пространство имён объекта класса
# >>> Table.__dict__
# mappingproxy({'__module__': '__main__', 'width': 0, 'depth': 0, 'height': 0, 'legs': 0, '__dict__': <attribute '__dict__' of 'Table' objects>, '__weakref__': <attribute '__weakref__' of 'Table' objects>, '__doc__': None})


# создание экземпляров
instance1 = Table()
instance2 = Table()

# объект экземпляра
# >>> instance1
# <__main__.Table object at 0x000001975046B950>
# >>>
# >>> type(instance1)
# <class '__main__.Table'>


# >>> instance1.width
# 0
# >>> instance1.depth
# 0
# >>> instance1.height
# 0
# >>>
# >>> instance2.width
# 0
# >>> instance2.depth
# 0
# >>> instance2.height
# 0

instance1.width = 2600
instance1.depth = 800
instance1.height = 590
instance1.legs = 5

instance2.width = 1200
instance2.depth = 1200
instance2.height = 810
instance2.legs = 4

# >>> instance1.width
# 2600
# >>> instance1.depth
# 800
# >>> instance1.height
# 590
# >>> instance1.legs
# 5
# >>>
# >>> instance2.width
# 1200
# >>> instance2.depth
# 1200
# >>> instance2.height
# 810
# >>> instance2.legs
# 4


# внутреннее пространство имён объекта экземпляра
# >>> instance1.__dict__
# {'width': 2600, 'depth': 800, 'height': 590, 'legs': 5}
# >>>
# >>> instance2.__dict__
# {'width': 1200, 'depth': 1200, 'height': 810, 'legs': 4}
# >>>


instance3 = Table()

# атрибуты экземпляра отсутствуют
# >>> instance3.__dict__
# {}

# область видимости расширяется до пространства имён класса — экземпляр получает доступ к атрибутам класса
# >>> instance3.width
# 0


# изменение атрибута класса
Table.thick = 0

# >>> Table.__dict__
# mappingproxy({'__module__': '__main__', 'width': 10, 'depth': 0, 'height': 0, 'legs': 0, '__dict__': <attribute '__dict__' of 'Table' objects>, '__weakref__': <attribute '__weakref__' of 'Table' objects>, '__doc__': None, 'thick': 0})
# >>>
# >>> instance1.thick
# 0
# >>> instance2.thick
# 0
# >>> instance3.thick
# 0

