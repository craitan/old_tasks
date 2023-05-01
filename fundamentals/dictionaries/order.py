order_dict = {}
order = input().split(' ')

while order[0] != 'buy':

    item = order[0]
    price = float(order[1])
    quantity = int(order[2])

    if item in order_dict:
        order_dict[item][0] = price
        order_dict[item][1] += quantity
    else:
        order_dict[item] = [price, quantity]

    order = input().split(' ')

for item in order_dict:
    total_price = order_dict[item][0] * order_dict[item][1]
    print(f"{item} -> {total_price:.2f}")

