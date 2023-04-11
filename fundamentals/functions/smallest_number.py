import sys


def smallest_number():
    small_number = sys.maxsize
    for x in range(3):
        number = int(input())

        if number < small_number:
            small_number = number

    return small_number


print(smallest_number())

# def small_number(a, b, c):
#     print(min((a, b, c)))
#
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# small_number(num1, num2, num3)
