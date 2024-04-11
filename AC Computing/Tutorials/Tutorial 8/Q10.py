def interleave_ver1 (n,k):
    interleaved = []
    length = len(n)
    for i in range(length):
        interleaved.append(n[i])
        interleaved.append(k[i])
    return tuple(interleaved)
    
tup1 = (1, 3, 5, 7, 9)
tup2 = (2, 4, 6, 8, 10)
tup3 = (30, 40, 50, 60, 70)