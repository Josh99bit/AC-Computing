from math import gcd

def egyptian(fraction):
    # Reduce the fraction to its lowest terms
    fraction = lowest_terms(fraction)
    numerator, denominator = fraction
    unitFractions = []
    
    # Continue subtracting unit fractions until the numerator is 1
    while numerator != 1:
        # Find the smallest unit fraction that can be subtracted
        newDenominator = denominator // numerator + 1
        unitFractions.append(newDenominator)
        
        # Update the fraction by subtracting the found unit fraction
        numerator = numerator * newDenominator - denominator
        denominator *= newDenominator
        
        # Reduce the new fraction to its lowest terms
        numerator, denominator = lowest_terms([numerator, denominator])

    # Add the final unit fraction
    unitFractions.append(denominator)
    
    return unitFractions