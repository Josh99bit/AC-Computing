def odd_even_sums (n):
    sumOfOdd=0
    sumOfEven=0
    for k in range(0,len(n)):
        #Add to sum of odds when index is even as index starts from 0
        if k % 2 == 0:
            sumOfOdd += n[k]
        else:
            sumOfEven += n[k]
    return (sumOfOdd,sumOfEven)
