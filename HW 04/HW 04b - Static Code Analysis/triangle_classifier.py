"""
Module for classifying triangles based on side lengths.

This module defines the `classify_triangle` function, which classifies
triangles as Equilateral, Isosceles, Scalene, or Right, based on the
lengths of the three sides. It also raises a ValueError for invalid
triangles or non-positive side lengths.
"""
def classify_triangle(a, b, c):
    """Classifies a triangle based on the lengths of its sides."""
    if any(side <= 0 for side in (a, b, c)):
        raise ValueError("Lengths must be positive")
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("This is not a working triangle")
    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles"
    if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
        return "Right"
    return "Scalene"
