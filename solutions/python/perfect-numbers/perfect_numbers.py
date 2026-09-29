"""perfect, abundant, or deficient number"""
def classify(number):
    """ A perfect number equals the sum of its positive divisors.
    
    Parameters:
        number (int): a positive integer.

    Returns:
        str: the classification of the input integer
    """
    if number < 1:
        raise ValueError('Classification is only possible for positive integers.')
    result = sum(num for num in range(1,number//2+1) if number%num==0)
    if result==number:
        return 'perfect'
    if result<number:
        return 'deficient'
    return 'abundant'
