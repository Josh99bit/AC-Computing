def divide_rat(f1, f2):
    if f2[0] == 0:
        return "Error: Divide by zero"
    else:
        result_numerator = f1[0] * f2[1]
        result_denominator = f1[1] * f2[0]
        return lowest_terms((result_numerator, result_denominator))
