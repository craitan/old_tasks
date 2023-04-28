text = input()
courses = {}

while ":" in text:
    data = text.split(":")
    name = data[0]
    id = data[1]
    curse = data[2]

    if curse not in courses:
        courses[curse] = {}

    courses[curse][id] = name
    text = input()

text = text.replace("_", " ")

for id in courses[text]:
    print(f'{courses[text][id]} - {id}')
