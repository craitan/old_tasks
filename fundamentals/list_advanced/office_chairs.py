n = int(input())
count = 0
condition = True
for x in range(1, n + 1):
    command = input().split(' ')
    chairs = command[0]
    people = int(command[1])

    if len(chairs) < people:
        condition = False
        chairs_needed = people - len(chairs)
        print(f"{chairs_needed} more chairs needed in room {x}")

    elif len(chairs) > people:
        count += len(chairs) - people

if condition:
    print(f"Game On, {count} free chairs left")
