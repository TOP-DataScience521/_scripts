from importlib.util import (
    module_from_spec,
    spec_from_file_location,
)
from sys import modules


file1 = 'how-to-import-me.py'
path1 = r'D:\G-Doc\TOP Academy\Data Science\521\scripts\libs'


module_name = 'how-to-import-me'

# создание объекта спецификации модуля (ModuleSpec)
spec = spec_from_file_location(module_name, fr'{path1}\{file1}')

# создание объекта модуля
module_obj = module_from_spec(spec)

# выполнение кода модуля
spec.loader.exec_module(module_obj)

# добавление объекта модуля в системный словарь всех импортированных модулей
modules[module_name] = module_obj


# >>> module_obj.a
# 123
# >>> module_obj.b
# 456

