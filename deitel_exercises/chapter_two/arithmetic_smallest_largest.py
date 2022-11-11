def smallest(num1, num2, num3):
    if num1 < num2 & num1 < num3:
        smallest_num = num1
    elif num2 < num1 & num2 < num3:
        smallest_num = num2
    else:
        smallest_num = num3
    print("The smallest value is", smallest_num)


def largest(num1, num2, num3):
    if num1 > num2 & num1 > num3:
        largest_num = num1
    elif num2 > num1 & num2 > num3:
        largest_num = num2
    else:
        largest_num = num3
    print("The largest value is", largest_num)


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
the_sum = number1 + number2 + number3
print("The sum is", the_sum)
average = the_sum // 3
print("The average value is", average)
product = number1 * number2 * number3
print("The product is", product)
smallest(number1, number2, number3)
largest(number1, number2, number3)
