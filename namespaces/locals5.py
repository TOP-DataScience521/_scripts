numbers = [10, 20, 40]


def list_change_1():
    numbers.append(60)


def list_change_2(arg_list):
    arg_list.append(100)


def list_change_3(arg_list):
    arg_list.append(200)
    return arg_list


breakpoint()

list_change_1()
list_change_2(numbers)
numbers_2 = list_change_3(numbers)

