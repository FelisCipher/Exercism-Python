def leap_year(year):
    """
    Finds whether a given year is leap year or not

    Parameters:
        year (int): Year to find whether it is leap year or not

    Returns:
        bool: True if it is leap year, False if not
    """
    
    if year%4==0 and not(year%100 ==0 and year%400 != 0):
        return True
    return False
