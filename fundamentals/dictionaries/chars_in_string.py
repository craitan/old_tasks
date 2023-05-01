text = input()

my_dict = {}

for x in text:
    if x == " ":
        continue
    elif x not in my_dict:
        my_dict[x] = 1
    elif x in my_dict:
        my_dict[x] += 1


for key, value in my_dict.items():
    print(f"{key} -> {value}")