def isprime(n):
    # First, check if n is greater than 1 since prime numbers are greater than 1
    if n <= 1:
        return False
    
    # Loop from 2 to the square root of n (inclusive) 
    # All non prime numbers are divisable by at least 1 number from 2 to square root of n (inclusive) 
    for k in range(2, int(n**0.5) + 1):
        # If n is divisible by any number in this range, it's not prime
        if n % k == 0:
            return False
    
    # If we've made it this far, n wasn't divisible by any number in the range,
    # so it's prime
    return True
