def add_rat(f1, f2):
    result_numerator = f1[0] * f2[1] + f2[0] * f1[1]
    result_denominator = f1[1] * f2[1]
    return lowest_terms((result_numerator, result_denominator))

def subtract_rat(f1, f2):
    result_numerator = f1[0] * f2[1] - f2[0] * f1[1]
    result_denominator = f1[1] * f2[1]
    return lowest_terms((result_numerator, result_denominator))

def multiply_rat(f1, f2):
    result_numerator = f1[0] * f2[0]
    result_denominator = f1[1] * f2[1]
    return lowest_terms((result_numerator, result_denominator))
