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