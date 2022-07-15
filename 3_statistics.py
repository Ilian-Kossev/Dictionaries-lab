command = input()
stock = {}
while not command == 'statistics':
    key, value = command.split(': ')
    if key not in stock.keys():
        stock[key] = int(value)
    else:
        stock[key] += int(value)
    command = input()
print('Products in stock:')
for key, value in stock.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(stock)}')
print(f'Total Quantity: {sum(stock.values())}')

