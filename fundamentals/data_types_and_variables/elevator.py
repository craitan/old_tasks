import math

people = int(input())
capacity = int(input())

answer = math.ceil(people / capacity)
print(answer)