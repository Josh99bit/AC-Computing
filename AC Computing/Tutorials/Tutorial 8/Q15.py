
def nric_fin_validator(nric):
    #conversion tables for both NRICs
    citizen={
        0:"J",
        1:"Z",
        2:"I",
        3:"H",
        4:"G",
        5:"F",
        6:"E",
        7:"D",
        8:"C",
        9:"B",
        10:"A"
    }

    longTermPass={
        0:"X",
        1:"W",
        2:"U",
        3:"T",
        4:"R",
        5:"Q",
        6:"P",
        7:"N",
        8:"M",
        9:"L",
        10:"K"
    }

    #Multiply by respective numbers
    firstLetter = nric[0]
    firstNum = int(nric[1]) * 2
    secondNum = int(nric[2]) * 7
    thirdNum = int(nric[3]) * 6
    fourthNum = int(nric[4]) * 5
    fifthNum = int(nric[5]) * 4
    sixthNum = int(nric[6]) * 3
    seventhNum = int(nric[7]) * 2
    lastLetter = nric[8]

    total = firstNum + secondNum + thirdNum + fourthNum + fifthNum + sixthNum + seventhNum

    #Add 4 to total when NRIC starts with T or G
    if firstLetter == "T" or firstLetter == "G":
        total += 4

    remainder = total % 11

    
    if firstLetter == "S" or firstLetter == "T":
        if citizen[remainder] == lastLetter:
            return True
        
    if firstLetter == "F" or firstLetter == "G":
        if longTermPass[remainder] == lastLetter:
            return True
        
    return False