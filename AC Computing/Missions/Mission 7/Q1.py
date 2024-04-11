def base2_to_base10(num):
    total = 0
    for n in range(len(num)):
        if num[n]=="1":
            total += 2 ** (len(num)-n-1)
    return str(total)
