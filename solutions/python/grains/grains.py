def square(number):
    """Calculate the number of grains on a given square.

    Parameters:
        number (int): given square.

    Returns:
        int: number of grains on a given square.
    """
    if number<=0 or number>64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)


def total():
    """Calculate the total number of grains on the chessboard.

    Returns:
        int: Total number of grains.
    """
    return (2**64)-1
