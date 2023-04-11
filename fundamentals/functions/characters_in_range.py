def char_range(a, b):
    ll = []
    for x in range(ord(a) + 1, ord(b)):
        ll.append(chr(x))

    result = " ".join(ll)

    return result


a = input()
b = input()

print(char_range(a, b))
