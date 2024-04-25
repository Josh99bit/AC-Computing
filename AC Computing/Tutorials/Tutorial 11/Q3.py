def sum_n_squares(n):
    # Base case
    if n == 1:
        return 1
    else:
        # Recursive case
        return n ** 2 + sum_n_squares(n - 1)

