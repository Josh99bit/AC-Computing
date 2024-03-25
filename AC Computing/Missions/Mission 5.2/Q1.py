def make_grid(keyword):
    # Initialize the grid and define the alphabet without the letter 'J'
    playfairGrid = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    # Create a unique keyword by removing duplicates and replacing 'J' with 'I'
    uniqueKeyword = ""
    for char in keyword.upper():
        if char == "J" and "I" not in uniqueKeyword:
            uniqueKeyword += "I"
        elif char in alphabet and char not in uniqueKeyword:
            uniqueKeyword += char
    
    # Gather remaining letters not in the unique keyword
    remainingLetters=[]
    for letter in alphabet:
        if letter not in uniqueKeyword:
            remainingLetters.append(letter)
    
    # Combine the unique keyword and remaining letters to form the cipher alphabet
    cipherAlphabet = list(uniqueKeyword) + remainingLetters
    
    # Split the cipher alphabet into rows of 5 for the Playfair grid
    row = []
    for letter in cipherAlphabet:
        row.append(letter)
        if len(row) == 5:
            playfairGrid.append(row)
            row = []
    

    return playfairGrid