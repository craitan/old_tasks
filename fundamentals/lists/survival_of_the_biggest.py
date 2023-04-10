numbers = input().split(' ')
n = int(input())

int_list = [int(num) for num in numbers]

for i in range(n):
    smallest_number = min(int_list)
    int_list.remove(smallest_number)

str_list = [str(num) for num in int_list]

print(', '.join(str_list))


# nums = input().split(' ')
# copy_nums = list(map(int, nums))
# count = int(input())
#
# for x in range(count):
#     current_min_element = min(copy_nums)
#     nums.remove(str(current_min_element))
#     copy_nums.remove(current_min_element)
#
# print(', '.join(nums))