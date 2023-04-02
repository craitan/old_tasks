n = int(input())
answer = 0
for x in range(n):
    char = input()
    answer += ord(char)

print(f"The sum equals: {answer}")
