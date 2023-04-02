ll = ['sand', 'water', 'fish', 'sun']
word = input()

count = [word.lower().count(x) for x in ll]
print(sum(count))