command = input()
count = 0
ll = ['cat', 'dog', 'coding', 'movie', 'CAT', 'DOG', 'CODING', 'MOVIE']
while command != "END":
    text = str(command)
    if text in ll:
        if text.isupper():
            count += 2
        else:
            count += 1

    command = input()
if count > 5:
    print("You need extra sleep")
else:
    print(count)