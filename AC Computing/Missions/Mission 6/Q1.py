def is_equivalent(fraction1, fraction2):

    result1 = fraction1[0] / fraction1[1]
    result2 = fraction2[0] / fraction2[1]

    if result1 == result2:
        return True
    else:
        return False
