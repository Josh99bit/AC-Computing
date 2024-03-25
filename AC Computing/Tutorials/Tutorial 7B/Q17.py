def remove_spaces(s):
    withoutSpaces = ""
    for n in s:
        if n != " ":
            withoutSpaces += n
    return withoutSpaces
