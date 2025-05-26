class Person:
    # атрибут класса
    age = 0
    
    # метод конструктор
    def __init__(instance, last_name_arg, first_name_arg):
        # атрибуты экземпляров
        instance.last_name = last_name_arg
        instance.first_name = first_name_arg


# instance = Class(*args, **kwargs)
# во время вызова объекта класса происходит вызов, который очень приближенно можно описать следующим образом:
# def metaclass.__call__(*args, **kwargs):
#     создание экземпляра (instance) со связью с классом (Class) и пустым пространством имён экземпляра
#     instance = object.__new__(Class)
#     вызов конструктора (__init__)
#     instance.__init__(*args, **kwargs)
#     возврат экземпляра 
#     return instance


anna = Person('Петрова', 'Анна')
andrey = Person('Прокопьев', 'Андрей')

# >>> anna.__dict__
# {'last_name': 'Петрова', 'first_name': 'Анна'}
# >>>
# >>> andrey.__dict__
# {'last_name': 'Прокопьев', 'first_name': 'Андрей'}

