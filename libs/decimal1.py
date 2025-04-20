from decimal import Decimal as dec


print(f'{dec = }')

print(
    '\n0.1 + 0.1 + 0.1 == 0.3',
    0.1 + 0.1 + 0.1 == 0.3,
    f'\n{dec(0.1) = }',
    "\ndec('0.1') + dec('0.1') + dec('0.1') == dec('0.3')",
    dec('0.1') + dec('0.1') + dec('0.1') == dec('0.3'),
    sep='\n'
)

