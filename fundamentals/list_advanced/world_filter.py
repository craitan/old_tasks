text = input().split(' ')

for word in text:
    if len(word) % 2 == 0:
        print(word)


even_words = [word for word in text if len(word) % 2 == 0]
print("\n".join(even_words))