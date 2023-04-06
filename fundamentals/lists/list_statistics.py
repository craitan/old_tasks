n = int(input())
pp = []
nn = []

for x in range(n):
    num = int(input())
    if num < 0:
        nn.append(num)
    else:
        pp.append(num)

print(pp)
print(nn)
print(f"Count of positives: {len(pp)}\nSum of negatives: {sum(nn)}")