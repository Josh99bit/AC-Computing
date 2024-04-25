def is_palindrome(s):
    # Base case: if the length of the string is 0 or 1, it's a palindrome
    if len(s) <= 1:
        return True
    else:
        # Compare the first and last characters of the string
        if s[0] == s[-1]:
            # If they are equal, recursively call is_palindrome with the substring excluding the first and last characters
            return is_palindrome(s[1:-1])
        else:
            # If the first and last characters are not equal, the string is not a palindrome
            return False
