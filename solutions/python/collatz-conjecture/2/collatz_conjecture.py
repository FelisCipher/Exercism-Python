"""Utilities for the Collatz Conjecture."""
def steps(number):
    """Determine number of steps it takes to reach 1 according to the rules of the Collatz Conjecture.

    Parameters:
        number (int): The given number.

    Returns:
        int: The number of steps took to reach 1.
    """
    if number<=0:
        raise ValueError('Only positive integers are allowed')
    count = 0
    while number>1:
        if number%2==0:
            number//=2
        else:
            number = number * 3 + 1
        count+=1
    return count
    