def palindrome():
    nums = list(map(int, input().split(', ')))
    for x in nums:
        if str(x) == str(x)[::-1]:
            print('True')
        else:
            print('False')



palindrome()