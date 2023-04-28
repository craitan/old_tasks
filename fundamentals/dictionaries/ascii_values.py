data = input().split(', ')
ascii_dict = {}
for x in data:
    ascii_dict[x] = ord(x)

print(ascii_dict)