products = {}

while True:
    command = input()

    if command == 'statistics':
        break

    key_value = command.split(": ")
    key = key_value[0]
    value = int(key_value[1])

    if key not in products:
        products[key] = value
    else:
        products[key] += value

print('Products in stock:')
for product, value in products.items():
    print(f"- {product}: {value}")

print(f'Total Products: {len(products)}')
print(f"Total Quantity: {sum(products.values())}")