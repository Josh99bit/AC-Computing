def count_vowels(string):
    vowels={"a" : 0 , "e" : 0 , "i" : 0, "o" : 0 , "u" : 0}
    for k in string:
        if k in ('a', 'e', 'i', 'o', 'u'):
            vowels[k]+=1
    return list(vowels.values())