from random import (
    choice,
    randrange as rr,
)


publishers = [rr(10**4, 10**5) for _ in range(3)]

for _ in range(12):
    print(f'9785{choice(publishers)}{rr(100, 1000)}2')

