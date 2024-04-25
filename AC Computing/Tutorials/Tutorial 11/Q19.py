def fib(n):
    # Base cases: the 0th and 1st Fibonacci numbers are 0 and 1 respectively
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: Fibonacci number at index n is the sum of the previous two Fibonacci numbers
        return fib(n - 1) + fib(n - 2)
