def count_words(filename):
    # Open the file in read mode
    file = open(filename,"r")
    # Extract all the lines into a list
    lines = file.readlines()
    # Close the file
    file.close()
    # Return the number of lines / items in the list
    return len(lines)

