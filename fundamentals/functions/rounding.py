def rounding(list):
    new_list = []

    for x in list:
        new_list.append(round(float(x)))

    return new_list


numbers = input().split(' ')
print(rounding(numbers))
