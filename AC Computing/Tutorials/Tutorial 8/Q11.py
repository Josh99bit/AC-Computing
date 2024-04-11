def interleave_ver2 (n,k):
    smallerLength = min(len(n),len(k))
    interleaved = []
    # zip() takes the 2 tuples and iterates through both 
    for i in zip(n,k):
        interleaved.append(i[0])
        interleaved.append(i[1])
    #Adds any remaining items from both lists
    interleaved += list(n[smallerLength::]) + list(k[smallerLength::])
    return tuple(interleaved)

tup1 = (1, 3, 5)
tup2 = (2, 4, 6, 8, 10, 12)
tup3 = (30, 40, 50)
