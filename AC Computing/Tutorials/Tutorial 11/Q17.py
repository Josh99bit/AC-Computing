def gcd(m, n):
    # Base case: If m equals n, then m is the GCD
    if m == n:
        return m
    # If m is greater than n, recursively call gcd with m-n and n
    elif m > n:
        return gcd(m - n, n)
    # If n is greater than m, recursively call gcd with m and n-m
    else:
        return gcd(m, n - m)