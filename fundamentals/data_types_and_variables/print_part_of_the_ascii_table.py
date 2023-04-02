num_1 = int(input())
num_2 = int(input())
answer = []
for x in range(num_1, num_2 + 1):
    answer.append(chr(x))

print(" ".join(answer))
