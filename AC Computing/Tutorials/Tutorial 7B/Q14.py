def gcd(m, n):
    while True:  # Start an infinite loop
        if m == n:
            # If m and n are equal, we have found the GCD
            return m
        elif m > n:
            # If m is greater than n, subtract n from m
            m -= n
        else:
            # If n is greater than m, subtract m from n
            n -= m
