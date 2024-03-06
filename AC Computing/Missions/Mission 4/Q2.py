
def collatz(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int(3*n+1)
def stopping_time(n):
    current = n
    count = 0
    while current != 1:
        current = collatz(current)
        count += 1
    return count
