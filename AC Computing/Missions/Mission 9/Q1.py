def poly_eval(p, x):
    total = 0
    for i in range(len(p)):
        total += p[i] * x ** i
    return total