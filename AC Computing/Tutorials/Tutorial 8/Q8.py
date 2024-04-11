def grab_tuple (n):
    for i in n:
        if type(i) == type(()):
            return i
