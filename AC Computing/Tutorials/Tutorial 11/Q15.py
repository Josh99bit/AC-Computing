def length(s):
    # Base case: if the string is empty
    if s == '':
        return 0
    else:
        # Recursive case: remove the first character and count the rest
        return 1 + length(s[1:])
