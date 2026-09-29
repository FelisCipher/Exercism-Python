def is_armstrong_number(number):
    """Determine the number is an armstrong number.

    Parameters:
        number (int): The given number.

    Returns:
        bool: True if the given number is armstrong number else False.
    """
    digits= str(number)
    length_digit = len(digits)
    result = sum(int(digit)**length_digit for digit in digits)
    return result==number
    