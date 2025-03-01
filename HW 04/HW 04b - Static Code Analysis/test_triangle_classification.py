"""Test case class for testing the triangle classification function."""
import unittest
from triangle_classifier import classify_triangle

"""This class has unit tests to check the classify_triangle function for input conditions."""
class TestTriangleClassification(unittest.TestCase):
    def test_equilateral(self):
        """
        Test case for equilateral triangles.
        
        This test verifies that the function correctly identifies an equilateral
        triangle when all three sides are equal.
        """
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")
    def test_isosceles(self):
        """
        Test case for isosceles triangles.
        
        This test verifies that the function correctly identifies an isosceles
        triangle when two sides are equal.
        """
        self.assertEqual(classify_triangle(3, 3, 4), "Isosceles")
    def test_scalene(self):
        """
        Test case for scalene triangles.
        
        This test verifies that the function correctly identifies a scalene
        triangle when all three sides are different.
        """
        self.assertEqual(classify_triangle(6, 8, 9), "Scalene")
    def test_right_triangle(self):
        """
        Test case for right triangles.
        
        This test verifies that the function correctly identifies a right triangle
        using the Pythagorean theorem.
        """
        self.assertEqual(classify_triangle(3, 4, 5), "Right")
    def test_invalid(self):
        """
        Test case for invalid triangles.
        
        This test verifies that the function raises a ValueError when invalid
        side lengths are provided.
        """
        with self.assertRaises(ValueError):
            classify_triangle(0, 4, 5)
        with self.assertRaises(ValueError):
            classify_triangle(-1, 1, 1)
if __name__ == '__main__':
    unittest.main()
