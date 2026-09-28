"""Score calculation of darts game"""
def score(x, y):
    """Determine the points scored in a single toss of a Darts game.

    Parameters:
        x (int): x-axis location.
        y (int): y-axis location.

    Returns:
        int: Score for the given location.
"""
    dist_from_center = x**2 + y**2
    if dist_from_center>100:
        return 0
    elif 25<dist_from_center<=100:
        return 1
    elif 1<dist_from_center<=25:
        return 5
    return 10
    
