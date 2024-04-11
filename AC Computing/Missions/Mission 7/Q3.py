def base10_to_base2(num):
    num = int(num)
    binary = ""
    
    while num >= 1:
        binary = str(num % 2) + binary
        num = num // 2
    return binary