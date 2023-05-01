contacts = input().split('-')
my_dict = {}
people = 0
condition = True
while condition:
    if contacts[0].isdigit():
        people = int(contacts[0])
        condition = False
        break

    for x in range(0, len(contacts), 2):
        contact = contacts[x]
        number = contacts[x + 1]
        if contact not in my_dict:
            my_dict[contact] = number
        else:
            my_dict[contact] = number

    contacts = input().split('-')


for x in range(people):
    name_to_check = input()
    if name_to_check in my_dict:
        print(f"{name_to_check} -> {my_dict[name_to_check]}")
    else:
        print(f"Contact {name_to_check} does not exist.")