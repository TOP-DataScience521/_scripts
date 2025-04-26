from sys import path


import_from_dir_path = r'D:\G-Doc\TOP Academy\Data Science\521\scripts\funcs'

path.insert(1, import_from_dir_path)

# >>> for p in path:
# ...     print(p)
# ...
# D:\G-Doc\TOP Academy\Data Science\521\scripts\namespaces
# D:\G-Doc\TOP Academy\Data Science\521\scripts\funcs
# C:\Python312\python312.zip
# C:\Python312\DLLs
# C:\Python312\Lib
# C:\Python312
# C:\Python312\Lib\site-packages


from recursion3 import extract_data_from_iterable

# >>> print(extract_data_from_iterable.__doc__)
# Принимает в качестве аргумента итерируемый объект с произвольным количеством уровней вложенности, и возвращает список всех неитерируемых объектов, собранных со всех уровней вложенности.

