first_string = input().split(', ')
second_string = input()

new_list = [el for el in first_string if el in second_string]

print(new_list)

