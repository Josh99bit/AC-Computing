def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

def sum_even_factorials(n):
    result = 1
    for i in range(1, n+1):
        if i % 2 == 0:
            result += factorial(i)
    return result