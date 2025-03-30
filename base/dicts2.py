menu = dict(zip(
    ['борщ', 'солянка', 'том-ям'], 
    (150, 135, 180)
))

# >>> menu
# {'борщ': 150, 'солянка': 135, 'том-ям': 180}

# >>> menu['борщ']
# 150
# >>>
# >>> menu['солянка']
# 135

for key in menu:
    print(type(key), repr(key))
print()

# <class 'str'> 'борщ'
# <class 'str'> 'солянка'
# <class 'str'> 'том-ям'

for value in menu.values():
    print(type(value), repr(value))
print()

# <class 'int'> 150
# <class 'int'> 135
# <class 'int'> 180

for elem in menu.items():
    print(type(elem), repr(elem))
print()

# <class 'tuple'> ('борщ', 150)
# <class 'tuple'> ('солянка', 135)
# <class 'tuple'> ('том-ям', 180)

for key, value in menu.items():
    print(type(key), repr(key), type(value), repr(value))
print()

# <class 'str'> 'борщ' <class 'int'> 150
# <class 'str'> 'солянка' <class 'int'> 135
# <class 'str'> 'том-ям' <class 'int'> 180

