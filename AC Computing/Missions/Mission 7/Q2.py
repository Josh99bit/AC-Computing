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

