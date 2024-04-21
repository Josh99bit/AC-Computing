def multiply_poly(p1, p2):
    # Initialize a dictionary to store the coefficients of the resulting polynomial
    coeffs = {}
    
    # Loop through each element in the first polynomial
    for n in range(len(p1)):
        # Loop through each element in the second polynomial
        for k in range(len(p2)):
            # Calculate the exponent for the current term by adding the indices
            exponent = n + k
            # Calculate the coefficient for the current term by multiplying the coefficients
            value = p1[n] * p2[k]
            
            # If the exponent already exists in the dictionary, add the current value to it
            if exponent in coeffs:
                coeffs[exponent] += value
            else:
                # Otherwise, create a new entry in the dictionary for this exponent
                coeffs[exponent] = value
    
    # Initialize a list to store the coefficients in order of increasing exponents
    result = []
    
    # Iterate over the exponents in sorted order to build the result list
    for k in sorted(coeffs.keys()):
        result.append(coeffs[k])
    
    # Remove trailing zeros from the coefficients list, but leave at least one zero if all are zero
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    # Return the resulting coefficients as a tuple
    return tuple(result)
