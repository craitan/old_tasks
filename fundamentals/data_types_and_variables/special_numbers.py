n = int(input())
str_n = str(n)

for x in range(1, n + 1):
    sum_of_dig = 0
    digits = x

    while digits > 0:
        sum_of_dig += digits % 10
        digits = int(digits / 10)

    if sum_of_dig == 5 or sum_of_dig == 7 or sum_of_dig == 11:
        print(f'{x} -> True')
    else:
        print(f'{x} -> False')
