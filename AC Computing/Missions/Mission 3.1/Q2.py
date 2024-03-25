
def reverse_and_add(n):
    #Makes input a string
    num = str(n)
    #Reverses the digits
    reverseNum = str(n[::-1])
    #Adds the 2 numbers together
    num = int(num) + int(n[::-1])
    return num
