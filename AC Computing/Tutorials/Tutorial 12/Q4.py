def rot13(string):
    result = ""

    # Iterate through each character in the input string
    for char in string:
        if char.isalpha():  # Check if the character is alphabetic
            unicode = ord(char)  # Get the Unicode value of the character
            newUnicode = unicode + 13  # Shift the Unicode value by 13 positions

            if char.isupper():  # Check if the character is uppercase
                if newUnicode > 90:  # Check if the new Unicode value exceeds the range of uppercase letters
                    newUnicode -= 26  # Wrap around to the beginning of the uppercase alphabet
                    
            else:  # Character is lowercase
                if newUnicode > 122:  # Check if the new Unicode value exceeds the range of lowercase letters
                    newUnicode -= 26  # Wrap around to the beginning of the lowercase alphabet

            newChar = chr(newUnicode)  # Convert the new Unicode value back to a character
            result += newChar  # Append the encrypted character to the result string

        else:  # Character is not alphabetic
            result += char  # Append the character unchanged to the result string

    return result
