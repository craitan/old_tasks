divisor = int(input())
boundary = int(input())
num = 0
for x in range(boundary + 1):
    if x % divisor == 0 and x > 0 and x <= boundary:
        num = x

print(num)
