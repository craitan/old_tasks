def password_validator(password):
    condition = True

    if 10 > len(password) < 6:
        condition = False
        print("Password must be between 6 and 10 characters")

    if not password.isalnum():
        condition = False
        print("Password must consist only of letters and digits")

    if sum(map(str.isdigit, password)) < 2:
        condition = False
        print("Password must have at least 2 digits")

    if condition:
        print("Password is valid")


text = input()

password_validator(text)
