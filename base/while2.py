n = 5
res = ''
while n > 0:
    word = input('слово: ')
    if not word:
        break
    res = (res if not res else f'{res} ') + word
    n = n - 1
else:
    print('записано пять слов')

print(res)

