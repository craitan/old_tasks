key = int(input())
n = int(input())
message = ''
for x in range(n):
    letter = input()
    new_letter = key + ord(letter)
    message += chr(new_letter)
print(message)
