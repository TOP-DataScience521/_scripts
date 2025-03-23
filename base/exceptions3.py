try:
    num1 = int(input('число 1: '))
    num2 = int(input('число 2: '))
    result = num1 / num2

except ValueError:
    print('некорректный ввод')

except ZeroDivisionError:
    print('деление на ноль невозможно')

else:
    print(f'{num1} / {num2} = {result}')



try:
    num1 = int(input('число 1: '))
    num2 = int(input('число 2: '))

except ValueError:
    print('некорректный ввод')

else:
    try:
        print(f'{num1} / {num2} = {num1 / num2}')
    except ZeroDivisionError:
        print('деление на ноль невозможно')

