def standard_deviation (nums):
    average = mean(nums)
    numberOfElements = len(nums)
    sumOfSquares=0
    for number in nums:
        sumOfSquares += (number - average) ** 2

    standardDeviation = (sumOfSquares / numberOfElements) ** (1/2)
    return round(standardDeviation,2)
