def is_happy_num(n, lst):
    result = 0

    # Calculate the sum of the squares of each digit of the number
    for k in str(n):
        result += int(k) ** 2

    # Check if the result is already in the list to detect cycles
    if result in lst:
        return False
    # Check if the result is 1, indicating that it's a happy number
    elif result == 1:
        return True
    else:
        # Recursively call is_happy_num with the new result and update the list with the intermediate result
        return is_happy_num(result, lst + [result])
