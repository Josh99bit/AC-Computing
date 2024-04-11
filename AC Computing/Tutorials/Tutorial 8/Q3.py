def swap_1st(n1,n2):
    updated1 = (n2[0], )+ n1[1::]
    updated2 = (n1[0], ) + n2[1::]
    return (updated1,updated2)
