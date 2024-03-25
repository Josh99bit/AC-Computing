def recycle(n,k):
    totalBottlesMade = 0
    scrap = n
    #While there is enough scrap to make new bottles
    while scrap >= k:
        newBottlesMade = scrap // k
        remainder = scrap % k
        totalBottlesMade += newBottlesMade
        #Scrap = remaining bottles + bottles made
        scrap = remainder + newBottlesMade
    return (totalBottlesMade, scrap)

print(recycle(16, 3))