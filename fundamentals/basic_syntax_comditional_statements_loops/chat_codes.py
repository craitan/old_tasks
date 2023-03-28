n = int(input())

for x in range(n):
    chat = int(input())
    if chat == 88:
        print('Hello')
    elif chat == 86:
        print('How are you?')
    elif chat != 88 and chat != 86 and chat < 88:
        print('GREAT!')
    elif chat > 88:
        print('Bye.')