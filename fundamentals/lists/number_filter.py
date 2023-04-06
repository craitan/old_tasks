n = int(input())
numbers = []
filtered = []

for i in range(n):
    num = int(input())
    numbers.append(num)

command = input()

if command == 'even':
    for x in numbers:
        if x % 2 == 0:
            filtered.append(x)
elif command == 'odd':
    for x in numbers:
        if x % 2 != 0:
            filtered.append(x)
elif command == 'negative':
    for x in numbers:
        if x < 0:
            filtered.append(x)
elif command == 'positive':
    for x in numbers:
        if x >= 0:
            filtered.append(x)

print(filtered)