def extract_vowels(string):
    extractedVowels = ""
    for n in string:
        if n in ('a', 'e', 'i', 'o', 'u'):
            extractedVowels += n
    return extractedVowels
