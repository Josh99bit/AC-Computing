def reverse_string(s):
    # Base case: if the string is empty or a single character, return it as is
    if len(s) <= 1:
        return s
    else:
        # Recursive case: call reverse_string on the substring from the second character to the end,
        # then append the first character to the result of the recursive call
        return reverse_string(s[1:]) + s[0]

