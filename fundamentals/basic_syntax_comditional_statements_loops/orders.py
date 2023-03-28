n = int(input())
total = 0
for x in range(1, n + 1):
    price = float(input())
    days = int(input())
    caps_need_per_day = int(input())
    if price <= 0 or days <= 0 or caps_need_per_day <= 0:
        continue
    final_price = price * days * caps_need_per_day
    total += final_price

    print(f"The price for the coffee is: ${final_price:.2f}")


print(f"Total: ${total:.2f}")