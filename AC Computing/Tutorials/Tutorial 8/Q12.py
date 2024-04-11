def interleave_ver3 (n,k):
    interleaved = []
    length = len(k)
    for i in range(length):
        interleaved.append(n[i*2])
        interleaved.append(n[i*2+1])
        interleaved.append(k[i])
    return tuple(interleaved)
    
tup1 = (1, 3, 5, 7, 9, 11, 13, 15)
tup2 = (2, 4, 6, 8)
tup3 = ('a', 'b', 'c', 'd')
tup4 = ('y', 'z')
