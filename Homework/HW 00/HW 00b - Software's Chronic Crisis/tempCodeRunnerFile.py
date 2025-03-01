import unittest
from triangle_classifier  import classify_triangle

class TestTriangleClassification(unittest.TestCase):
    
    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")
    
    def test_isosceles(self):
        self.assertEqual(classify_triangle(3, 3, 4), "Isosceles")
    
    def test_scalene(self):
        self.assertEqual(classify_triangle(6, 15, 22), "Scalene")
    
    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right")
    
    def test_invalid(self):
        self.assertEqual(classify_triangle(0, 4, 5), "Invalid triangle sides")
        self.assertEqual(classify_triangle(-1, 1, 1), "Invalid triangle sides")

if __name__ == '__main__':
    unittest.main()
