budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25 / 4
total_price = flour_price + eggs_price + milk_price
flour = 0
eggs = 0
milk = 0
bread = 0
colored_eggs = 0

while budget > total_price:
    budget -= total_price
    flour += 1
    eggs += 1
    milk += 1

while flour > 0:
    bread += 1
    flour -= 1

for x in range(1, bread + 1):
    if x % 3 == 0:
        colored_eggs += 3
        colored_eggs -= x - 2
    else:
        colored_eggs += 3

print(f"You made {bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
