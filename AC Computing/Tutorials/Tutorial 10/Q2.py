def remove_numbers(fileName):
    # Open the input file in read mode and create a variable for it
    inputFile = open(fileName, "r")
    
    # Read lines from the input file
    lines = inputFile.readlines()
    
    # Open the output file in write mode and create a variable for it
    outputFile = open("output.txt", "w")
    
    # Iterate over each line in the list of lines
    for line in lines:
        # Check if the stripped line is numeric
        if not line.strip().isnumeric():
            # If the line is not numeric, write it to the output file
            outputFile.write(line)
    
    # Close the input and output files
    inputFile.close()
    outputFile.close()


