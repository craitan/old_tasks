random_string = input()
n = int(input())

new_string = lambda x, y: x * y

result = new_string(random_string, n)

print(result)