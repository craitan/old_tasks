size = int(input())
days = int(input())
coins = 0
for x in range(1, days + 1):

    if x % 10 == 0:
        size -= 2
    if x % 15 == 0:
        size += 5

    coins += 50
    coins -= 2 * size

    if x % 3 == 0:
        coins -= 3 * size
    if x % 5 == 0:
        coins += 20 * size
        if x % 3 == 0:
            coins -= 2 * size
print(f"{size} companions received {int(coins / size)} coins each.")
