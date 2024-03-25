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

def improved_egyptian(f):
    smallestFraction=None
    numerator = f[0]
    denominator = f[1]
    #loops through all numbers from 1 to numerator-1
    for n in range(1, numerator):
        valid = True
        #Gets both numerators
        numerator1 = n
        numerator2 = numerator - n
        #creates both fractions
        fraction1 = egyptian([numerator1, denominator])
        fraction2 = egyptian([numerator2, denominator])

        #check for common denominators
        for k in fraction1:
            if k in fraction2:
                valid = False

        if valid:
            #Add fractions
            fraction = sorted(fraction1 + fraction2)
            if smallestFraction:
                if smallestFraction[-1] > fraction[-1]:
                    smallestFraction = fraction
                elif smallestFraction[-1] == fraction [-1]:
                    if len(fraction) < len(smallestFraction):
                        smallestFraction = fraction
            else:
                smallestFraction=sorted(fraction1+fraction2)
    return smallestFraction
