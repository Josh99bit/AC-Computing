def findFactors(n):
    factors=set([n])
    for i in range(1 ,(n // 2) + 2):
        if n % i == 0:
            factors.add(i)
    return factors

def gcd(N1,N2):
    factorsOfN1=findFactors(N1)
    factorsOfN2=findFactors(N2)
    LCF = 1
    for n in factorsOfN1:
        if n in factorsOfN2:
            if n > LCF:
                LDF = n
    return LDF
            

