"""Raindrop sounds"""
def convert(number):
    """Convert a number to raindrop sound.

    Parameters:
        number(int): The given number.

    Returns:
        str: Corresponding raindrop sound of the given number.
"""
    word=''
    if number%3==0:
        word+='Pling'
    if number%5==0:
        word+='Plang'
    if number%7==0:
        word+='Plong'
    return word or str(number)
    