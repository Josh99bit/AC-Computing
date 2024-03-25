def count_char(string, x):
    count = 0
    for n in string:
        if n == x:
            count += 1
    return count