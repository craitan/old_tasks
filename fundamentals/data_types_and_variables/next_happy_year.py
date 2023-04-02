year = int(input())

while True:
    year += 1
    if len(set(str(year))) == 4:
        break

print(year)

# We add + 1 to the year we transformed into set of str cuz in sets there are only unique values when we get to a
# year that is with for different numbers the len of the set == 4 we break the while cycle and print the year cuz
# there are 4 unique numbers in the set.
