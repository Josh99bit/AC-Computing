def max_stopping_time(n):
    max=stopping_time(1)
    pos=1
    for i in range(1, n+1):
        stoppingTime=stopping_time(i)
        if stoppingTime>max:
            max=stoppingTime
            pos=i
    return [pos,max]
def max_max_num_reached(n):
    max=max_num_reached(1)
    pos=1
    for i in range(1, n+1):
        m=max_num_reached(i)
        if m>max:
            max=m
            pos=i
    return [pos,max]
