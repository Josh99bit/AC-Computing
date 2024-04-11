def operate_elevator(t1, t2):
    # Initialize the starting position and time taken for each elevator
    # Using None for index 0 to align elevator numbers with indexes of list
    elevatorPositions = [None,1,1]
    elevatorTimes = [None,0,0]

    # Process each instruction
    for instruction in (t1, t2):
        elevator, start, destination = instruction
        
        # Calculate the time taken for the current instruction
        # Time = (Absolute difference between current position and start level +
        #         Absolute difference between start level and destination level) * 2
        time_taken = (abs(elevatorPositions[elevator] - start) + abs(start - destination)) * 2
        
        # Update the time taken and the elevator's final position
        elevatorTimes[elevator] += time_taken
        elevatorPositions[elevator] = destination

    # Prepare the output tuple
    result = (
        (1, elevatorTimes[1], elevatorPositions[1]),
        (2, elevatorTimes[2], elevatorPositions[2])
    )

    return result


print(operate_elevator((2, 5, 8), (1, 9, 7)))
print(operate_elevator((1, 9, 10), (2, 12, 1)))
print(operate_elevator((1, 9, 7), (1, 3, 10)))