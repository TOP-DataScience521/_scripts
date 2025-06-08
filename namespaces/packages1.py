# namespaces
# │   ...
# │   packages1.py
# │
# │   # пакет
# ├───dir1
# │   ├───__init__.py
# │   └───module1.py
# │
# │   # просто каталог
# └───dir2
#     └───module2.py

print(f'точка входа: {__name__!r}')


import dir1


dir1.func()

