n = int(input())
searched_word = input()
ll1 = []
ll2 = []

for i in range(n):
    string_input = str(input())
    ll1.append(string_input)
    if searched_word in string_input:
        ll2.append(string_input)

print(ll1)
print(ll2)
