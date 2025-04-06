def add(num1, num2):
    result = num1 + num2
    # print(type(num1), type(num2), type(result))
    print(f'{num1} + {num2} = {result}')
    return result


a = add(5, 15)
b = add(-3, -7)
c = add(a, b)

# 5 + 15 = 20
# -3 + -7 = -10
# 20 + -10 = 10


print(add('яблоко', 'груша'))

# <class 'str'> <class 'str'> <class 'str'>
# яблоко + груша = яблокогруша
# яблокогруша

