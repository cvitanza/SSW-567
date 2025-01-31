def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid triangle sides"
    
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            return "Isosceles and Right"
        return "Isosceles"
    elif a != b and b != c and a != c:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            return "Scalene and Right"
        return "Scalene"
    else:
        return "Not a triangle"
