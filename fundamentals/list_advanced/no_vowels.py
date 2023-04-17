ll = ['a', 'o', 'u', 'e', 'i']

text = input()

new_text = "".join([x for x in text if x not in ll])

print(new_text)