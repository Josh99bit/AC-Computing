def add_poly(p1, p2):
    # Calculate the maximum length of the two polynomial tuples
    max_length = max(len(p1), len(p2))
    
    # Extend both polynomials to the maximum length by appending zeros as necessary
    p1_extended = list(p1) + [0] * (max_length - len(p1))
    p2_extended = list(p2) + [0] * (max_length - len(p2))
    
    # Initialize an empty list to store the result coefficients
    coeffs = []
    
    # Add corresponding coefficients from both polynomials
    for x, y in zip(p1_extended, p2_extended):
        coeffs.append(x + y)
    
    # Remove trailing zeros from the coefficients list, but leave at least one zero if all are zero
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    
    # Return an empty tuple if the resulting polynomial is zero
    if not coeffs or (len(coeffs) == 1 and coeffs[0] == 0):
        return ()
    
    # Return the resulting polynomial as a tuple
    return tuple(coeffs)



def subtract_poly(p1, p2):
    # Calculate the maximum length of the two polynomial tuples
    max_length = max(len(p1), len(p2))
    
    # Extend both polynomials to the maximum length by appending zeros as necessary
    p1_extended = list(p1) + [0] * (max_length - len(p1))
    p2_extended = list(p2) + [0] * (max_length - len(p2))
    
    # Initialize an empty list to store the result coefficients
    coeffs = []
    
    # Subtract corresponding coefficients from the first polynomial by the second
    for x, y in zip(p1_extended, p2_extended):
        coeffs.append(x - y)
    
    # Remove trailing zeros from the coefficients list, but leave at least one zero if all are zero
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    
    # Return an empty tuple if the resulting polynomial is zero
    if not coeffs or (len(coeffs) == 1 and coeffs[0] == 0):
        return ()
    
    # Return the resulting polynomial as a tuple
    return tuple(coeffs)
