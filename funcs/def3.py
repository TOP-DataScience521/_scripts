def calc(num1, num2, sign='+'):
    if sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    elif sign == '*':
        return num1 * num2
    elif sign == '/':
        return num1 / num2


# >>> calc(50, 22, '-')
# 28
# >>> calc(50, 22)
# 72

# >>> calc(50)
# TypeError: calc() missing 1 required positional argument: 'num2'
# >>>
# >>> calc(5, 9, '*', True)
# TypeError: calc() takes from 2 to 3 positional arguments but 4 were given

# >>> calc(num1=12, sign='*', num2=8)
# 96
# >>> calc(sign='/', num2=3, num1=999)
# 333.0

# >>> calc(30, num2=44, sign='-')
# -14
# >>> calc(30, sign='-', num2=44)
# -14
# >>> calc(sign='-', 30, num2=44)
# SyntaxError: positional argument follows keyword argument

# >>> calc(10, num1=20, num=30, sign='-')
# TypeError: calc() got multiple values for argument 'num1'

