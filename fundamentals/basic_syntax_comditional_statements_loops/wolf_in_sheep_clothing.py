string_ig = input().split(", ")
new_list = (list(string_ig))

for i in range(len(new_list) - 1, -1, -1):
    if new_list[i] == "wolf" and i == len(new_list) - 1:
        print("Please go away and stop eating my sheep")
        break
    elif new_list[i] == "sheep" and new_list[i - 1] == "wolf":
        print(f"Oi! Sheep number {len(new_list)-i}! You are about to be eaten by a wolf!")
        break