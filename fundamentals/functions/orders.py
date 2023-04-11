# def orders(product, quantity):
#     if product == 'coffee':
#         return f"{quantity * 1.5:.2f}"
#     elif product == 'water':
#         return f"{quantity * 1.0:.2f}"
#     elif product == 'coke':
#         return f"{quantity * 1.4:.2f}"
#     elif product == 'snacks':
#         return f"{quantity * 2.0:.2f}"
#
#
# products = input()
# products_quantity = int(input())
#
# print(orders(products, products_quantity))


def total_price(product, quantity):
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1
    elif product == "coke":
        price = 1.4
    else:
        price = 2

    print(f"{quantity * price:.2f}")


product = input()
quantity = int(input())

total_price(product, quantity)