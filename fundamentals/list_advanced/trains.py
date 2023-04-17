n = int(input())
train = [0 for x in range(n)]


while True:
    text = input()

    if text == "End":
        break

    commands = text.split(" ")
    command = commands[0]
    if command == "add":
        people = int(commands[1])
        train[-1] += people

    elif command == "insert":
        position = int(commands[1])
        people = int(commands[2])
        train[position] += int(commands[2])

    elif command == "leave":
        position = int(commands[1])
        people = int(commands[2])
        train[position] -= int(commands[2])

print(train)