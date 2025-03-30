text = '''Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements). If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).

If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings (for example, '1,,2'.split(',') returns ['1', '', '2']). The sep argument may consist of multiple characters as a single delimiter (to split with multiple delimiters, use re.split()). Splitting an empty string with a specified separator returns [''].'''

separator = '\n\n'

result1 = text.split(separator)

result2 = []
start = 0
for i in range(len(text)):
    if text[i:i+len(separator)] == separator:
        result2 = result2 + [text[start:i]]
        start = i + len(separator)
result2 = result2 + [text[start:]]

try:
    assert result1 == result2
except AssertionError:
    print('результаты не совпадают')
else:
    print('результаты совпадают')

