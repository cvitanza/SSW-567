"""
Module to classify triangles based on the lengths of their sides.
"""

def classify_triangle(a, b, c):
    """
    Classifies a triangle based on the lengths of its sides.
    
    Args:
        a (float): Length of side a.
        b (float): Length of side b.
        c (float): Length of side c.
        
    Returns:
        str: The classification of the triangle ('Equilateral', 'Isosceles', 
             'Scalene', 'Scalene and Right', 'Isosceles and Right', or 
             'Not a triangle').
    """
    if any(side <= 0 for side in (a, b, c)):
        raise ValueError("Lengths must be positive")
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("The provided sides do not form a valid triangle")
    
    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
            return "Isosceles and Right"
        return "Isosceles"
    if a != b and b != c and a != c:
        if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
            return "Scalene and Right"
        return "Scalene"
    
    return "Not a triangle"
