def get_hundredth (n1, n2, n3):
    #Puts numbers in a list
    l=[n1, n2, n3]
    hundredths=[]
    for i in l:
        #If less than 100, return 0
        if i < 100:
            hundredths.append(0)
        else:
            hundredth = int(i/100)
            hundredths.append(hundredth)
            
            
    return tuple(hundredths)


print(get_hundredth(1749, 802, 91996))