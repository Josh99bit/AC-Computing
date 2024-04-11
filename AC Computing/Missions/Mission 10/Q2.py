def sieve(n):
    nonPrime = set()
    prime=[]
    # Loop through all numbers
    for i in range(2, n+1):
        # Check if number in set of non prime
        if i not in nonPrime:
            # Add i to prime
            prime.append(i)
            # Add all mulitiples of i smallet than n
            for k in range(2,(n // i) +1):
                nonPrime.add(k * i)
    return prime