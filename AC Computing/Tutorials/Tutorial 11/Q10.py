def recursive_sum(x):
    # Base case: if x <= 2, return 1
    if x <= 2:
        return 1
    else:
        # Determine the recursive sum based on whether x is even or odd
        if x % 2 == 0:
            return recursive_sum(x-1) + recursive_sum(x-2) + recursive_sum(x-3)
        else:
            return recursive_sum(x-1) + recursive_sum(x-2)

