words = ['в', 'начале', 'было', 'слово']

separator = ' '

result1 = separator.join(words)

result2 = ''
for word in words[:-1]:
    result2 = result2 + word + separator
result2 = result2 + words[-1]

try:
    assert result1 == result2
except AssertionError:
    print('результаты не совпадают')
else:
    print('результаты совпадают')

