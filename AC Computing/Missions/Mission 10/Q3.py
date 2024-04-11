def pseudoprime(x):
    pseudoprimes = 0
    for n in range(2, x + 1):
        # Check if 2**n - 2 is divisible by n, and n is not prime
        if (2**n - 2) % n == 0 and not isprime(n):
            pseudoprimes+=1
    return pseudoprimes
