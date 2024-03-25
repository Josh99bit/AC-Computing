def count_substring(string, x):
    if x:  # Ensure the substring is not empty
        count = 0
        length_of_x = len(x)

        # Loop through the string, checking each substring of the same length as x
        for i in range(len(string) - length_of_x + 1):
            # If the substring matches x, increment the count
            if string[i:i+length_of_x] == x:
                count += 1
        return count
    else:
        return "I cannot count emptiness"