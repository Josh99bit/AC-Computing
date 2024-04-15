def keyword_decipher(text, keyword):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    unique_keyword = ""
    for char in keyword:
        if char not in unique_keyword and char in alphabets:
            unique_keyword += char
    
    remaining_letters = []
    for letter in alphabets:
         if letter not in unique_keyword:
             remaining_letters.append(letter)

    cipher_alphabet = list(unique_keyword) + remaining_letters

    result = ""
    for char in text:
        if char in alphabets:
            position = cipher_alphabet.index(char)
            result += alphabets[position]
        else:
            result += char

    return result
