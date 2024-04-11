def countprime(n, r):
    # Get all primes from 2 to n
    allPrimes = sieve(n)
    remainderR= 0
    # Loop through all primes
    for n in allPrimes:
        # Check if reminder is r
        if n % 4  == r:
            remainderR+=1
    return remainderR