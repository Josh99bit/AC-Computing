def base10_to_baseN(base, num):
    num = int(num)
    alphabets = {"10":"A","11":"B","12":"C","13":"D","14":"E","15":"F"}
    baseN = ""
    while num >= 1:
        n = str(num % base)
        if n in alphabets:
            n = alphabets[n]
        baseN = n + baseN
        num = num // base
    return baseN
