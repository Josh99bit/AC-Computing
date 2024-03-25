def up_to_n (n):
    total = 0
    sumOfNums = 0
    factorial = 1
    count=1
    while total < n:
        #Update the factorial
        factorial *= count
        #Update the sum 
        sumOfNums += count
        #Add factorial over sum
        total += factorial / sumOfNums
        count += 1
        
    return count-1