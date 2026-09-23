def equilateral(sides):
    """Determine if a triangle is equilateral

    Parameters:
        sides (list): three sides of triangle.
        
    Returns:
        bool: True if all 3 sides are equal and greater than 0.
    """
    return sides[0]==sides[1]==sides[2]>0

def isosceles(sides):
    """Determine if a triangle is isosceles

    Parameters:
        sides (list): three sides of triangle.
        
    Returns:
        bool: True if all 2 or 3 sides are equal and greater than 0.
    """
    sorted_sides= sorted(sides)
    return len(set(sides))!=3 and sum(sorted_sides[:2])>=sorted_sides[2]


def scalene(sides):
    """Determine if a triangle is scalene

    Parameters:
        sides (list): three sides of triangle.
        
    Returns:
        bool: True if all 3 sides are unequal and greater than 0.
    """
    sorted_sides= sorted(sides)
    return len(set(sides))==3 and sum(sorted_sides[:2])>=sorted_sides[2]