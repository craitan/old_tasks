def perfect(n):
    sums = 0
    for i in range(1, n):
        if (n % i == 0):
            sums += i

    if (sums == n):
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())
perfect(number)
