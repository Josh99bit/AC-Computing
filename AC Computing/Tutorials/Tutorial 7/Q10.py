
def star_wars(n):
    result = ""
    for n in range(1, n+1):
        if n % 2 == 0:
            result += "-->"
        else:
            result += "->"
    return result