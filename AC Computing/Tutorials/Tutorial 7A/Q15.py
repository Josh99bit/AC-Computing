def min_and_max(L):
    minimum = 99999999999
    maximum = -99999999999
    for n in L:
        if n > maximum:
            maximum = n
        if n < minimum:
            minimum = n
    return [minimum, maximum]
