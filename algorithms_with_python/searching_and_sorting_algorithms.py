ll = [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""find the number 4 in ll and return its index with linear search and using enumerate()"""


def linear_search(ll, target):
    for index, value in enumerate(ll):
        if value == target:
            return index
    return -1


print(linear_search(ll, 12))

print(linear_search(ll, 4))

"""find the number 4 in ll and return its index with binary search"""


def binary_search(ll, target):
    left = 0
    right = len(ll) - 1
    while left <= right:
        mid = (left + right) // 2
        if ll[mid] == target:
            return mid
        elif ll[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


print(binary_search(ll, 6))
"""Selection sort"""
nums = [6, 10, 7, 5, 2, 4, 9, 8, 3]

for idx in range(len(nums)):
    min_number = nums[idx]
    min_idx = idx
    for next_idx in range(idx + 1, len(nums)):
        next_number = nums[next_idx]
        if next_number < min_number:
            min_number = next_number
            min_idx = next_idx
    nums[idx], nums[min_idx] = nums[min_idx], nums[idx]

print(*nums)

"""Bubble sort"""
is_sorted = False
counter = 0
while not is_sorted:
    is_sorted = True
    for idx in range(1, len(nums) - counter):
        if nums[idx] < nums[idx - 1]:
            nums[idx], nums[idx - 1] = nums[idx - 1], nums[idx]
            is_sorted = False
    counter += 1

print(*nums)
