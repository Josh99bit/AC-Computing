def division_remainder (n, k):
    if k == 0:
        return "Division by Zero Error!"
    else:
        remainder = n
        while remainder >= k:
            remainder-= k
        return remainder

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
