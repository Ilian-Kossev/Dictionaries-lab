input_sequence = input().split(' ')
bakery = {}
for i in range(0, len(input_sequence), 2):
    key = input_sequence[i]
    value = input_sequence[i + 1]
    bakery[key] = int(value)
print(bakery)

