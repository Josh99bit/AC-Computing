def count_steps(n):
    #Sets up counter
    count=0
    found = False
    #Loops forever until found
    while  not found:
        if is_palindrome(n):
            found =  True
        else: 
            n = reverse_and_add(n)
            count += 1
    return count
