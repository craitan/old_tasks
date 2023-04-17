number_list = list(map(int, input().split(', ')))
new_list = []
for x in range(len(number_list)):
    if number_list[x] % 2 == 0:
        new_list.append(x)

print(new_list)