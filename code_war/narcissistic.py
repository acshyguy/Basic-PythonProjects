def narcissistic(value):
    # Code away
    sum = 0
    power = len(str(value))
    for i in range(value):
        sum += pow(i, power)

    if sum == value:
        return True
    return False

print(narcissistic(7))