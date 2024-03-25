def playfair_cipher(message, keyword):
    result = ""
    grid = make_grid(keyword) 
    message_pairs = break_pair(message)  

    # Encrypt each pair
    for pair in message_pairs:
        pos1 = pos2 = [0, 0]  # Initialize positions
        encryptedPos1 = encryptedPos2 = [0, 0]  # Initialize encrypted positions

        # Find positions of the pair letters in the grid
        for r in range(5):
            for c in range(5):
                if grid[r][c] == pair[0]:
                    pos1 = [r, c]
                if grid[r][c] == pair[1]:
                    pos2 = [r, c]
        
        # Encrypt based on the positions
        # %5 wraps back to 0
        if pos1[0] == pos2[0]:  # Same row
            encryptedPos1 = [pos1[0], (pos1[1] + 1) % 5]
            encryptedPos2 = [pos2[0], (pos2[1] + 1) % 5]

        elif pos1[1] == pos2[1]:  # Same column
            encryptedPos1 = [(pos1[0] + 1) % 5, pos1[1]]
            encryptedPos2 = [(pos2[0] + 1) % 5, pos2[1]]

        else:  # Rectangle form
            encryptedPos1 = [pos1[0], pos2[1]]
            encryptedPos2 = [pos2[0], pos1[1]]

        # Extract the encrypted characters from the grid
        encrypted1 = grid[encryptedPos1[0]][encryptedPos1[1]]
        encrypted2 = grid[encryptedPos2[0]][encryptedPos2[1]]

        # Append to the result string
        result += encrypted1 + encrypted2

    return result
