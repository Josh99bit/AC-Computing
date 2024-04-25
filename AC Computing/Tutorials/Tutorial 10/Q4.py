def hotdogs(filename):
    # Open the file using a variable in read mode
    file = open(filename, "r")
    
    winner = None
    maxEaten = 0

    # Process each line in the file
    for line in file.readlines():
        # Remove any leading or trailing whitespace and split the line by comma and space
        name, eaten = line.strip().split(", ")
        eaten = int(eaten)  # Convert the number of eaten hot dogs from string to integer

        # Check if the current number of eaten hot dogs is greater than the max found so far
        if eaten > maxEaten:
            maxEaten = eaten
            winner = name

    # Close the file after reading all lines
    file.close()

    # Output the result
    print("Winner:", winner)
    print("Number of hot dogs eaten:", maxEaten)

