def factorial(n):
    # Base case
    if n == 0:
        return 1
    
    else:
        # Recursive case
        return n * factorial(n - 1)