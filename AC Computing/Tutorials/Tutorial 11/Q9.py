def f(n): 
    # Base case
    if n < 3:
        return n
    else:
        # Recursive case
        return f(n-1) + 2*f(n-2) + 3*f(n-3)
