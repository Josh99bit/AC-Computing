def whole_number (n):
    wholeNumbers = []
    for number in n:
        if int(number) == number:
            wholeNumbers.append(number)
    return tuple(wholeNumbers)