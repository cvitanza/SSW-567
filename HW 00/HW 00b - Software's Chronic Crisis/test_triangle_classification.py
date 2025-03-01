import unittest
from triangle_classifier import classify_triangle

class TestTriangleClassification(unittest.TestCase):
    """
    Test cases for the classify_triangle function.
    """

    def test_equilateral(self):
        """
        Test case for equilateral triangles.
        """
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")
    
    def test_isosceles(self):
        """
        Test case for isosceles triangles.
        """
        self.assertEqual(classify_triangle(3, 3, 4), "Isosceles")
    
    def test_scalene(self):
        """
        Test case for scalene triangles.
        """
        self.assertEqual(classify_triangle(6, 8, 9), "Scalene") 
    
    def test_right_triangle(self):
        """
        Test case for right triangles.
        """
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right")
    
    def test_invalid(self):
        """
        Test case for invalid triangle sides.
        """
        with self.assertRaises(ValueError):
            classify_triangle(0, 4, 5)
        with self.assertRaises(ValueError):
            classify_triangle(-1, 1, 1)

if __name__ == '__main__':
    unittest.main()
