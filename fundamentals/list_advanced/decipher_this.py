text = input().split(' ')
ll = []
str1 = ""
str2 = ""

new_word = ""

for word in text:

    for ch in word:
        if not ch.isalpha():
            str1 += ch
        else:
            str2 += ch

    new_word = chr(int(str1)) + str2
    if len(new_word) > 2:
        last_word = new_word[:1] + new_word[-1] + new_word[2:-1] + new_word[1]
    else:
        last_word = new_word
    ll.append(last_word)
    str1 = ""
    str2 = ""

print(" ".join(ll))