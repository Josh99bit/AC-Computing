def divisible_by_nine (n):
    string = str(n)
    sumOfDigits = 0
    for digit in string:
        sumOfDigits += int(digit)

    remainder = division_remainder(sumOfDigits,9)
    if remainder == 0:
        return True
    else:
        return False