latin_1 = {}

start = ord('A')
amnt = 26

for code in range(start, start+amnt):
    latin_1[code] = chr(code)

# >>> latin_1
# {65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z'}


value = 'X'
for k, v in latin_1.items():
    if v == value:
        print(k)
        break


latin_1_reversed = {}
for k, v in latin_1.items():
    latin_1_reversed[v] = k
print(latin_1_reversed[value])

