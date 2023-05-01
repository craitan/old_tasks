text = input()
my_dict = {}
list_of_metal = []
while text != 'stop':

    list_of_metal.append(text)
    text = input()

for x in range(0, len(list_of_metal), 2):
    metal = list_of_metal[x]
    quantity = int(list_of_metal[x + 1])
    if metal not in my_dict:
        my_dict[metal] = quantity
    else:
        my_dict[metal] += quantity


for metal, quantity in my_dict.items():
    print(f"{metal} -> {quantity}")
