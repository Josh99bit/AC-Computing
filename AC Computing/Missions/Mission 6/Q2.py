from math import gcd

def lowest_terms(f):
    numerator, denominator = f
    common_divisor = gcd(numerator, denominator)
    
    # Reduce the fraction to its lowest terms
    reduced_numerator = numerator // common_divisor
    reduced_denominator = denominator // common_divisor

    # Ensure the denominator is positive
    if reduced_denominator < 0:
        reduced_numerator = -reduced_numerator
        reduced_denominator = -reduced_denominator

    return [reduced_numerator, reduced_denominator]
