n = int(input())

for x in range(n):
    string = str(input())
    if '_' in string or '.' in string or ',' in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")