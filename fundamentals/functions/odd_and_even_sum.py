def odd_even():
    numbers = input()
    odd = [int(x) for x in numbers if int(x) % 2 != 0]

    even = [int(x) for x in numbers if int(x) % 2 == 0]

    return f"Odd sum = {sum(odd)}, Even sum = {sum(even)}"

print(odd_even())