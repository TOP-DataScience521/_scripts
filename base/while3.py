while True:
    num = input('очередное число: ')
    if not num:
        break
    num = int(num)
    print(num**2)

print()

while True:
    try:
        num = int(input('введите число: '))
    except ValueError:
        print('! некорректный ввод\n! вводите только символы цифр')
    else:
        break

