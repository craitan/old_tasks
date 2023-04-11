# def grades(grade):
#     if 2.00 <= grade <= 2.99:
#         print('Fail')
#     elif 3.00 <= grade <= 3.49:
#         print('Poor')
#     elif 3.50 <= grade <= 4.49:
#         print('Good')
#     elif 4.50 <= grade <= 5.49:
#         print('Very Good')
#     elif 5.50 <= grade <= 6.00:
#         print('Excellent')
#
# grades(float(input()))


def grades(grade):

    if grade < 3:
        return ('Fail')
    elif grade <= 3.5:
        return ('Poor')
    elif grade <= 4.5:
        return ('Good')
    elif grade <= 5.5:
        return ('Very Good')
    else:
        return ('Excellent')

print(grades(float(input())))