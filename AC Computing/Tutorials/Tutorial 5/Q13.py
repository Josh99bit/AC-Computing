def BMI (L):
    heightInMeters=L[0]/100
    weightInKg=L[1]
    return round(weightInKg / (heightInMeters ** 2), 2)
