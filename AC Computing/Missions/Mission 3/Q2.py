def is_palindrome(s):
    formattedS = remove_spaces(remove_punc(s)).upper()
    length = len(formattedS)

    if length % 2 == 0:
        h = int(length / 2)
        firstHalf = formattedS[0:h]
        secondHalf = formattedS[h:length]
        reversedSecondHalf=secondHalf[::-1]
        return (firstHalf == reversedSecondHalf)
    else:
        h = int(length // 2)
        firstHalf = formattedS[0:h]
        secondHalf = formattedS[h+1:length]
        reversedSecondHalf=secondHalf[::-1]
        return (firstHalf == reversedSecondHalf)
    
