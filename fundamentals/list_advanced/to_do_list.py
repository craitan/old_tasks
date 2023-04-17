to_do = [0] * 10
while True:
    notes = input()

    if notes == "End":
        break

    commands = notes.split('-')

    position = int(commands[0]) - 1
    task = commands[1]
    to_do.pop(position)
    to_do.insert(position, task)


result = [task for task in to_do if task != 0]

print(result)