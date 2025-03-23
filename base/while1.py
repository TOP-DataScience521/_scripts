# while <условное_выражение>:
#     <тело_цикла>
# else:
#     <блок_для_корректного_завершения_цикла>


n = 10

while n > 0:
    print(n, end=' ')
    n = n - 1

print(f'\nвсё\n')


text = 'abc def  ! ghi'

while not text.isalpha():
    print(text)
    text = text.replace(' ', '', 1)
    text = text.replace('.', '', 1)
    text = text.replace(',', '', 1)
    text = text.replace('!', '', 1)
    text = text.replace('?', '', 1)

print(text)

