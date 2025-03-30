url = 'www.example.com'

chars_to_strip = 'cmowz.'

result1 = url.strip(chars_to_strip)

result2 = ''
start = 0
end = len(url)

for i in range(len(url)):
    if url[i] not in chars_to_strip:
        start = i
        break

for j in range(-1, -len(url)-1, -1):
    if url[j] not in chars_to_strip:
        end = j + 1
        break

result2 = url[start:end]

try:
    assert result1 == result2
except AssertionError:
    print('результаты не совпадают')
else:
    print('результаты совпадают')

