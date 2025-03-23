try:
    number = int(input('число: '))

except ValueError:
    print('некорректный ввод\nвводите только символы цифр')

else:
    print(number**3)


# число: 123
# 1860867


# число: 23 56z
# некорректный ввод
# вводите только символы цифр
# >>>
# >>> number
# NameError: name 'number' is not defined


number = input('число: ').strip()

if number and (number.isdecimal() or number[0] == '-' and number[1:].isdecimal()):
    number = int(number)
    print(number**3)

else:
    print('некорректный ввод\nвводите только символы цифр')

