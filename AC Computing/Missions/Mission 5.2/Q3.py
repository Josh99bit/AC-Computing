def break_pair(inputString):
    # Initialize variables for processing the string
    cipherPairs = []
    currentPair = ""
    pairCount = 0
    
    for character in inputString:
        # Substitute 'J' with 'I' 
        if character == "J":
            character = "I"
        
        # If the same character repeats, insert 'X' between and start a new pair
        if character == currentPair:
            currentPair += "X"
            cipherPairs.append(currentPair)
            currentPair = character
            pairCount = 0
        else:
            currentPair += character
        pairCount += 1
        
        # If we've constructed a complete pair, add it to the list and reset for the next pair
        if pairCount == 2:
            cipherPairs.append(currentPair)
            currentPair = ""
            pairCount = 0
    
    # If there's a single character left without a pair, add 'X' to complete the pair
    if pairCount == 1:
        cipherPairs.append(currentPair + "X")
    
    return cipherPairs