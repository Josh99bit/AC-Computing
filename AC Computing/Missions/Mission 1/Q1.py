def not1(x):
    return nand(x, x)
def and1(x, y):
    return nand(nand(x,y),True)
def or1(x, y):
    return nand(nand(x,True),nand(y,True))