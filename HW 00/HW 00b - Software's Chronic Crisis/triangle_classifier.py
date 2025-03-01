def classify_triangle(a, b, c):
    if any(side <= 0 for side in (a, b, c)):
        raise ValueError("Lengths must be positive")
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("The provided sides do not form a valid triangle")
    
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        if (a**2 + b**2 == c**2 )or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
            return "Isosceles and Right"
        return "Isosceles"
    elif a != b and b != c and a != c:
        if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
            return "Scalene and Right"
        return "Scalene"
    else:
        return "Not a triangle"
