word = input()
ll = []
for x in range(len(word)):
    if word[x].isupper():
        ll.append(x)

print(ll)
