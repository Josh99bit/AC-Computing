def exponentiation(x, e):
    # Base case: if exponent is 0, return 1
    if e == 0:
        return 1
    else:
        # Recursive case: return base * power of base to exponent - 1
        return x * exponentiation(x, e - 1)
