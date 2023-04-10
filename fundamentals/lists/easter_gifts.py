gifts = input().split(' ')

while True:
    commands = input()
    if commands == "No Money":
        break

    new_commands = commands.split(' ')
    command = new_commands[0]
    gift = new_commands[1]

    if command == 'OutOfStock':
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = 'None'
    elif command == 'Required':
        if len(gifts) > int(new_commands[2]) > 0:
            gifts[int(new_commands[2])] = gift
    elif command == 'JustInCase':
        gifts[len(gifts) - 1] = gift

for gift in gifts:
    if gift != 'None':
        print(gift, end=" ")
