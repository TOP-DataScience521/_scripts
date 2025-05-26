from pprint import pp


class Test:
    
    # связанный метод
    def do_smth(parameter):
        print(f'{parameter = }')


# >>> Test
# <class '__main__.Test'>
# >>>
# >>> pp(Test.__dict__)
# mappingproxy({'__module__': '__main__',
#               'do_smth': <function Test.do_smth at 0x00000225933639C0>,
#               '__dict__': <attribute '__dict__' of 'Test' objects>,
#               '__weakref__': <attribute '__weakref__' of 'Test' objects>,
#               '__doc__': None})
# >>>
# >>> Test.do_smth
# <function Test.do_smth at 0x00000225933639C0>
# >>>
# >>> Test.do_smth(None)
# parameter = None


instance = Test()

# >>> instance
# <__main__.Test object at 0x0000022593341A30>
# >>>
# >>> instance.__dict__
# {}

# >>> instance.do_smth
# <bound method Test.do_smth of <__main__.Test object at 0x0000022593341A30>>
# >>>
# >>> instance.do_smth()
# parameter = <__main__.Test object at 0x0000022593341A30>
# >>>
# >>> instance.do_smth(None)
# TypeError: Test.do_smth() takes 1 positional argument but 2 were given



# вызов метода от экземпляра можно рассматривать как следующую подмену вызова:
# экземпляр.метод(*позиционные, **ключевые) --> Класс.функция(экземпляр, *позиционные, **ключевые)


# >>> Test.do_smth(instance)
# parameter = <__main__.Test object at 0x0000022593341A30>


