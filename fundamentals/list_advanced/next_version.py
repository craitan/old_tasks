version = input().split('.')

str_version = "".join(version)

new_version = ".".join(str(int(str_version) + 1))

print(new_version)