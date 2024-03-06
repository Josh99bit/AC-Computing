def max_stopping_time(n):
    maximum=stopping_time(1)
    number=1
    for i in range(1, n+1):
        stoppingTime = stopping_time(i)
        if stoppingTime > maximum:
            maximum = stoppingTime
            num = i
    return [num, maximum]


def max_max_num_reached(n):
    maximum=max_num_reached(1)
    num=1
    for i in range(1, n+1):
        maximumNumReached = max_num_reached(i)
        if maximumNumReached > maximum:
            maximum = maximumNumReached
            num = i
    return [num, maximum]