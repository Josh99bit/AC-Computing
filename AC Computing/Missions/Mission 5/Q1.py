def keyword_cipher(text, keyword):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    unique_keyword = ""
    for char in keyword:
        if char not in unique_keyword and char in alphabets:
            unique_keyword += char

    remaining_letters = [letter for letter in alphabets if letter not in unique_keyword]
    cipher_alphabet = list(unique_keyword) + remaining_letters

    result = ""
    for char in text:
        if char in alphabets:
            position = alphabets.index(char)
            result += cipher_alphabet[position]
        else:
            result += char

    return result