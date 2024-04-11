def even_rank (n):
    evenIndex = []
    for k in range(1, len(n), 2):
        evenIndex.append(n[k])

    return tuple(evenIndex)

