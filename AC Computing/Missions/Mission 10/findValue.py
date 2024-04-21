def sieve(n):
    nonPrime = set()
    prime = [2]
    for i in range(3, n+1,2):
        if i not in nonPrime:
            prime.append(i)
            for k in range(2,(n // i) +1):
                nonPrime.add(k * i)
    return prime

def smallest(upperLimit):
    # Counter for primes with 4k+3 and 4k+1
    r1 = 0
    r3 = 0
    # Find all primes between 2 and the upper limit
    allPrimes = sieve(upperLimit)
    for n in allPrimes:
        if n%4 == 1:
            r1 += 1
        elif n % 4 == 3:
            r3 += 1
        if r1 > r3:
            return n
        
# Taking upper limit as 10 Million
print(smallest(10000000))

# Complexity of smallest O(n log log n)