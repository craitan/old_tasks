ll = input().split(' ')
zz = input()
words = [word for word in ll if word == word[::-1]]
lz = ll.count(zz)
print(words)
print(f"Found palindrome {lz} times")