input_sequence = input().split()
item_to_search_list = input().split()
stock = {}
for i in range(0, len(input_sequence), 2):
    key = input_sequence[i]
    value = input_sequence[i + 1]
    stock[key] = int(value)
for item in item_to_search_list:
    if item in stock:
        print(f'We have {stock[item]} of {item} left')
    else:
        print(f"Sorry, we don't have {item}")
