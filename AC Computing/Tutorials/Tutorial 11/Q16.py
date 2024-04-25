def flatten(tup):
    # Initialize an empty tuple to store the flattened elements
    newTup = ()

    # Iterate through each element of the tuple
    for n in tup:
        # If the element is itself a tuple, recursively flatten it
        if isinstance(n, tuple):
            newTup += flatten(n)  # Concatenate the flattened tuple to newTup
        else:
            # If the element is not a tuple, add it directly to newTup
            newTup += (n,)

    # Return the flattened tuple
    return newTup
