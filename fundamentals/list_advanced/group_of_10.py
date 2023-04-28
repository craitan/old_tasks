def groups(numbers):
    current_grp = 10
    grp_list = []
    while numbers:
        result = list(filter(lambda x: x <= current_grp, numbers))
        grp_list.append(result)
        print(f"Group of {current_grp}'s: {result}")

        for x in result:
            if x in numbers:
                numbers.remove(x)
        current_grp += 10

numbers = list(map(int, input().split(", ")))
groups(numbers)