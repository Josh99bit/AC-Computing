def power(a,b):
    # Handle the special case where both base and exponent are zero
    if a == 0:
        if b == 0:
            return "Undefined!"  # Mathematically, 0^0 is undefined
        elif b < 0:
            return "Zero Division Error!"  # Cannot divide by zero, i.e., 1/(0^-b) is undefined

    # Return 1 for any base if exponent is 0 since any number to the power of 0 is 1
    if b == 0:
        return 1
    
    # Handle negative exponents by using the reciprocal of the base raised to the positive counterpart
    elif b < 0:
        return 1 / power(a, -b)
    
    # Recursively calculate power for positive exponents
    else:
        return a * power(a, b-1)
