number = int(input("Enter a number: "))
number_square = number ** 2


def check(number, number_square):
    power = len(str(number))
    return number_square % 10 ** power


if check(number, number_square) == number:
    print(number," is the same with the last digit of it square")
else:
    print(number," is ot the same with the last digit of it square")
