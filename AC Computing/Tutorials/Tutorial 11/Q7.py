def sum_odd_n(n):
    # Base case: if n is 1, return 1 (the first odd number)
    if n == 1:
        return 1
    else:
        # Recursive case: calculate the nth odd number and add it to the sum of the previous odd numbers
        return (2 * n - 1) + sum_odd_n(n - 1)

