def rom_to_num(roman):
    # Mapping of Roman numerals to their decimal values.
    value_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    # Iterate through each character in the Roman numeral string.
    for char in reversed(roman):
        value = value_map[char]  # Get the decimal value of the Roman numeral.
        
        # If the value is less than the previous value, subtract it; otherwise, add it.
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total
