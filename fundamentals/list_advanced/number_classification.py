numbers = input().split(', ')

positive_numbers = ", ".join([num for num in numbers if int(num) >= 0])

negative_numbers = ", ".join([num for num in numbers if int(num) < 0])

even_numbers = ", ".join([num for num in numbers if int(num) % 2 == 0])

odd_numbers = ", ".join([num for num in numbers if int(num) % 2 != 0])

print(f'Positive: {positive_numbers}\nNegative: {negative_numbers}\nEven: {even_numbers}\nOdd: {odd_numbers}')

