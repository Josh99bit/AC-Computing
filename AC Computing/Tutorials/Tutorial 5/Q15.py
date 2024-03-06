def asc_desc_check(L):
    ascending = True
    descending = True
    previousNumber = None
    for n in L:
        if previousNumber:
            if previousNumber > n:
                ascending = False
            elif previousNumber < n:
                descending = False
        previousNumber = n

    if ascending:
        return "Ascending"
    elif descending:
        return "Descending"
    else:
        return "Not sorted"
