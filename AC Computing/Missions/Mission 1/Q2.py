def not2(x):
    return nor(x, x)
def and2(x, y):
    return nor(nor(x,False),nor(y,False))
def or2(x, y):
    return nor(nor(x,y),nor(x,y))