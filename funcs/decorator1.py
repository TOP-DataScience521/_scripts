def decorator_func(func_obj):
    print('начало выполнения функции декоратора')
    
    def wrapper():
        print('начало выполнения функции обёртки')
        func_obj()
        print('конец выполнения функции обёртки')
    
    print('конец выполнения функции декоратора')
    return wrapper

