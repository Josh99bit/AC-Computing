punc="\'!\"#$%&()*+,-./:;<=>?@[\\]^_`\{\}~|"
def remove_punc(s):
    withoutPunc=""
    for n in s:
        if n not in punc:
            withoutPunc += n
    return withoutPunc