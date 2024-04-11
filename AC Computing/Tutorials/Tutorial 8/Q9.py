def grab_tuples (n):
    listOfTuples = []
    for i in n:
        if type(i) == type(()):
            listOfTuples.append(i)
    return tuple(listOfTuples)