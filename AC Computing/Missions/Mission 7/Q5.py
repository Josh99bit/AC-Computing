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

def baseN_to_base10(base, num):
    alphabets = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    total = 0
    for n in range(len(num)):
        number = num[n]
        # Check if charecter is an alphabet
        if number in alphabets:
            number = alphabets[number]
        else:
            number = int(number)
            
        total += number * (base ** (len(num)-n-1))
    return str(total)

def baseN_to_baseM(baseN, baseM, num):
    base10 = baseN_to_base10(baseN, num)
    baseM = base10_to_baseN(baseM, base10)
    return baseM
