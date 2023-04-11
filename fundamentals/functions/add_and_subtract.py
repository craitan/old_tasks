def sum_numbers(a, b):
    return  a + b

def substract(current_num, c):
    return current_num - c


num1 = int(input())
num2 = int(input())
num3 = int(input())

result = substract(sum_numbers(num1, num2), num3)
print(result)