def is_palindrome(s):
    newS=remove_spaces(remove_punc(s)).upper()
    length=len(newS)
    if length%2==0:
        h=int(length/2)
        firstHalf=newS[0:h]
        secondHalf=newS[h:length][::-1]
        return (firstHalf==secondHalf)
    else:
        h=int(length//2)
        firstHalf=newS[0:h]
        secondHalf=newS[h+1:length][::-1]
        return (firstHalf==secondHalf)
    