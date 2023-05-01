n = int(input())
register_dict = {}

for x in range(n):
    text = input()
    register = text.split(' ')
    command = register[0]
    name = register[1]

    if command == 'register':
        car = register[2]
        if name not in register_dict:
            register_dict[name] = car
            print(f"{name} registered {car} successfully")
        else:
            print(f"ERROR: already registered with plate number {car}")
    elif command == 'unregister':
        if name not in register_dict:
            print(f"ERROR: user {name} not found")
        else:
            register_dict.pop(name)
            print(f"{name} unregistered successfully")

for name, car in register_dict.items():
    print(f"{name} => {car}")