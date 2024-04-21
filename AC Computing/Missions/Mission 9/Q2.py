def derivative(p):
    dydx = ()
    for n in range(1,len(p)):
        dydx += (p[n] * n,)
    return dydx
