def count_digit(n):
    # Base case: when the number reduces to 0
    if n == 0:
        return 0
    else:
        # Recursive case: divide the number by 10 and count each step
        return 1 + count_digit(n // 10)