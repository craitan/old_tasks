n = int(input())
capacity = 0
for x in range(n):
    liters = int(input())
    if capacity + liters <= 255:
        capacity += liters
        continue

    print("Insufficient capacity!")

print(capacity)
