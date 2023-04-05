n = int(input())
text = ''
for x in range(n):
    line = input()

    if line == '(':
        text += line
    elif line == ')':
        text += line
        if text == '()':
            text = ''

if len(text) > 0:
    print('UNBALANCED')
else:
    print('BALANCED')
