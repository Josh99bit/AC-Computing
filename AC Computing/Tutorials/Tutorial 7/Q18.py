def number_pattern(i):
    for n in range(1, i + 1):
        numberOfHash = i - n
        print(numberOfHash*"# " + ( str(n) + " ") * n)