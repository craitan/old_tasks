stocks = input().split(' ')

products = input().split(' ')
stock = {}

for x in range(0, len(stocks), 2):
    key = stocks[x]
    value = stocks[x + 1]
    stock[key] = int(value)

for product in products:

    if product not in stock:
        print(f"Sorry, we don't have {product}")
    else:
        print(f"We have {stock[product]} of {product} left")
