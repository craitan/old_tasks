courses_dict = {}

while True:
    text = input().split(" : ")

    if text[0] == 'end':
        break

    course = text[0]
    name = text[1]

    if course not in courses_dict:
        courses_dict[course] = []
        courses_dict[course].append(name)
    else:
        courses_dict[course].append(name)

for course, names in courses_dict.items():
    print(f"{course}: {len(courses_dict[course])}")
    for name in names:
        print(f"-- {name}")