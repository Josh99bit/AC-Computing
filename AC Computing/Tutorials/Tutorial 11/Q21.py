def calculate_cost(tup):
    # Base case: if the tuple is empty, return 0
    if tup == ():
        return 0
    else:
        # Dictionary containing item codes and their prices
        prices = {1: 4.15, 2: 8.3, 3: 12.45, 4: 7.9, 5: 12.05, 6: 16.2}
        
        # Calculate the cost of the first item in the tuple and add it to the cost of the rest of the items
        return prices[tup[0]] + calculate_cost(tup[1:])
