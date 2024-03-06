def BMI (L):
    heightInMeters=L[0]/100
    weightInKg=L[1]
    return round(weightInKg / (heightInMeters ** 2), 2)

def body_category (L):
    bmi = BMI(L)
    if bmi < 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    else:
        return "Overweight"