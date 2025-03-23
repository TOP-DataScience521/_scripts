sent = input('введите предложение: ')

# print(id(sent))

for i in range(len(sent)):
    if sent[i].isalpha():
        break

try:
    sent = sent[:i] + sent[i].upper() + sent[i+1:]
except NameError:
    print('! предложение не должно быть пустым')
else:
    if sent[-1] not in '.!?':
        try:
            if sent[-2] not in '.!?':
                sent = sent + '.'
        except IndexError:
            sent = sent + '.'
    
    print(sent)
    
    # print(id(sent))

