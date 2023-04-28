data = input().split(' ')

symbol_dict = {}


for symbol in data:
    if symbol.lower() not in symbol_dict:
        symbol_dict[symbol.lower()] = 1
    else:
        symbol_dict[symbol.lower()] += 1


for key, value in symbol_dict.items():
    if value % 2 != 0:
        print(key, end=" ")