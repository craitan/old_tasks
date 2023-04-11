numbers = map(float, input().split(' '))
new_list = []
for x in numbers:
    new_numbers = abs(float(x))
    new_list.append(new_numbers)
print(new_list)