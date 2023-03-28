command = input()

while command != "End":
    text = str(command)
    if text != 'SoftUni':
        new_string = ''
        for x in text:
            new_string += x *2
        print(new_string)

    command = input()
