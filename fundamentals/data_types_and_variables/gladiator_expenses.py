fights_lost = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_breaks = 0
sword_breaks = 0
shield_breaks = 0
armor_breaks = 0

for x in range(1, fights_lost + 1):

    if x % 2 == 0:
        helmet_breaks += 1
    if x % 3 == 0:
        sword_breaks += 1
        if x % 2 == 0:
            shield_breaks += 1
            if shield_breaks % 2 == 0:
                armor_breaks += 1


aureus = (helmet_breaks * helmet_price) + (shield_breaks * shield_price) + (armor_breaks * armor_price) + (sword_breaks * sword_price)

print(f"Gladiator expenses: {aureus:.2f} aureus")