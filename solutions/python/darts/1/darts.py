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
    elif dist_from_center>25 and dist_from_center<=100:
        return 1
    elif dist_from_center>1 and dist_from_center<=25:
        return 5
    return 10
    
