var = [10, 20, 50]


def show_var_1():
    # доступ к глобальной var
    print(var)


def show_var_2():
    # доступ к локальной var
    var = 0.015
    print(var)


def show_var_3():
    # доступ к глобальной var невозможен, потому что должна быть (но ещё не) создана локальная var
    print(var)
    var = 0.015
    print(var)


show_var_1()
show_var_2()
show_var_3()

