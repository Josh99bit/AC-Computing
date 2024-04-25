def capitalise_word(fileName):
    # Open the input file in read mode and assign it to a variable
    inputFile = open(fileName, "r")
    
    # Read lines from the input file
    lines = inputFile.readlines()
    
    # Open the output file in write mode and assign it to a variable
    outputFile = open("output.txt", "w")
    
    # Iterate over each line
    for line in lines:
        # Capitalize all alphabetic characters in the line
        capitalizedLine = "".join([char.upper() if char.isalpha() else char for char in line])
        # Write the capitalized line to the output file
        outputFile.write(capitalizedLine)
    
    # Close both the input and output files
    inputFile.close()
    outputFile.close()

