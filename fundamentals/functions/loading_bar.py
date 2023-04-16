def printing(number):
    percentages = int(number / 10) * "%"
    dots = int((100 - number) / 10) * '.'
    if number < 100:
        print(f"{number}% [{percentages}{dots}]")
        print("Still loading...")
    elif number == 100:
        print(f"{number}% Complete!")
        print(f"[{percentages}]")

printing(int(input()))