n = int(input())

value = 0
data = ''
for i in range(n):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_weight / snowball_time) ** snowball_quality

    if value < snowball_value:
        value = snowball_value
        data = f"{snowball_weight} : {snowball_time} = {int(snowball_value)} ({snowball_quality})"

print(data)