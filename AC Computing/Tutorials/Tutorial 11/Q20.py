def is_fib(n):
    # Calculate the expressions under the square roots for both conditions
    expr1 = (5 * n ** 2 + 4)**0.5
    expr2 = (5 * n ** 2 - 4)**0.5

    # Check if either expression yields a perfect square
    if int(expr1) == expr1 or int(expr2) == expr2:
        return True
    else:
        return False