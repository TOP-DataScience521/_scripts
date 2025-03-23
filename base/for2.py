msg = input('введите сообщение: ')

for ch in msg:
    if ch == '.':
        print('найдена точка')
        break
else:
    print('точка не найдена')

