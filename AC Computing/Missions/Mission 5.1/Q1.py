#Edited version of keyword_cipher from Mission 5 Q1
def create_cipher(keyword):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    unique_keyword = ""
    for char in keyword:
        if char not in unique_keyword and char in alphabets:
            unique_keyword += char

    remaining_letters = [letter for letter in alphabets if letter not in unique_keyword]
    cipher_alphabet = list(unique_keyword) + remaining_letters

    return cipher_alphabet

def keywords_cipher(text, keywords):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    # Create a list of cipher alphabets using the create_cipher function
    cipher_alphabets = []
    for keyword in keywords:
        cipher_alphabets.append(create_cipher(keyword))

    # Initialize a counter to keep track of which cipher alphabet to use
    cipher_index = 0

    for char in text:
        if char in alphabet:
            # Use the current cipher alphabet to encode the character
            original_index = alphabet.index(char)
            current_cipher=cipher_alphabets[cipher_index]
            ciphered_char = current_cipher[original_index]

            # Append the encoded character, preserving the original case
            result += ciphered_char

            # Move to the next cipher alphabet, cycling back to the first if necessary
            cipher_index = (cipher_index + 1) % len(cipher_alphabets)
        else:
            # If the character is not in the alphabet, append it unchanged
            result += char

    return result
