def merge_tuple(tuple1, tuple2):
    # Initialize indices for iterating through both tuples
    index1, index2 = 0, 0
    merged_tuple = ()

    # Loop until we reach the end of one of the tuples
    while index1 < len(tuple1) and index2 < len(tuple2):
        if tuple1[index1] <= tuple2[index2]:
            merged_tuple += (tuple1[index1],)
            index1 += 1
        else:
            merged_tuple += (tuple2[index2],)
            index2 += 1
    
    # If there are remaining elements in tuple1, add them to merged_tuple
    while index1 < len(tuple1):
        merged_tuple += (tuple1[index1],)
        index1 += 1
    
    # If there are remaining elements in tuple2, add them to merged_tuple
    while index2 < len(tuple2):
        merged_tuple += (tuple2[index2],)
        index2 += 1

    return merged_tuple

tup1 = (-5, 10, 65, 100, 200)
tup2 = (-20, 30, 40, 65, 80, 95)
tup3 = (-1000, 1000)
