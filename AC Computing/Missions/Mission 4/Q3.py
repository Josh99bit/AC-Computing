def max_num_reached(n):
    current = n
    maximum = 1
    while current != 1:
        current = collatz(current)
        if current > maximum:
            maximum = current
    return maximum