first_word = input()
second_word = input()
for x in range(len(first_word)):
    if first_word[x] != second_word[x]:
        replacement = second_word[x]
        word = first_word[0:x] + replacement + first_word[x + 1:]
        first_word = word
        print(first_word)