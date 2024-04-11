def num_to_rom(number):
    # Define the mapping of decimal values to Roman numerals.
    value_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    # Start with an empty Roman numeral.
    roman_numeral = ""

    # Iterate over the value map, subtracting and adding to the Roman numeral string.
    for value, numeral in value_map:
        while number >= value:
            number -= value
            roman_numeral += numeral

    return roman_numeral