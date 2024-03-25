def is_palindrome(n):
    # Convert the input number to a string
    n = str(n)
    
    # Get the length of the string
    length = len(n)
    
    # Check if the length is even
    if length % 2 == 0:
        # Calculate the midpoint for even length
        midpoint = int(length / 2)
        
        # Split the string into two halves
        firstHalf = n[0:midpoint]
        secondHalf = n[midpoint:length][::-1]  # Reverse the second half
        
        # Check if both halves are equal
        return (firstHalf == secondHalf)
    else:
        # Calculate the midpoint for odd length, excluding the middle character
        midpoint = int(length // 2)
        
        # Split the string into two halves, excluding the middle character
        firstHalf = n[0:midpoint]
        secondHalf = n[midpoint + 1:length][::-1]  # Reverse the second half
        
        # Check if both halves are equal
        return (firstHalf == secondHalf)