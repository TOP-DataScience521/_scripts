class ListOfFunctions(list):
    def __call__(self):
        results = []
        for f in self:
            results.append(f())
        return results


def func1():
    print('вызвана функция 1')

def func2():
    print('вызвана функция 2')

def func3():
    print('вызвана функция 3')


lof = ListOfFunctions([func1, func2, func3])

