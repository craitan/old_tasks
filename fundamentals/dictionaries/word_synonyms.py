n = int(input())

my_dict = {}

for x in range(n):
    word = input()
    synonym = input()

    if word not in my_dict:
        my_dict[word] = []
        my_dict[word].append(synonym)
    else:
        my_dict[word].append(synonym)

for word, synonym in my_dict.items():
    print(f'{word} - {", ".join(synonym)}')