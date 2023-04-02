n = int(input())

for x in range(n):
    for y in range(n):
        for z in range(n):
            print(f'{chr(97 + x)}{chr(97 + y)}{chr(97 + z)}')