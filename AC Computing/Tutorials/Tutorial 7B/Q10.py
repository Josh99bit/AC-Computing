def division_remainder (n, k):
    if k == 0:
        return "Division by Zero Error!"
    else:
        remainder = n
        while remainder >= k:
            remainder-= k
        return remainder
