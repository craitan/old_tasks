num_list = input().split(', ')
beggars = int(input())
result_sum = 0
result_list = []

for n in range(beggars):
    for i in range(n, len(num_list), beggars):
        result_sum += int(num_list[i])
    result_list.append(result_sum)
    result_sum = 0

print(result_list)