var = 123

try:
    current_module_namespace = globals()
    for identificator, value in current_module_namespace.items():
        print(f'{identificator!r}: {value!r}')
except RuntimeError:
    print('\n! невозможно изменение словаря во время итерирования по нему\n')

