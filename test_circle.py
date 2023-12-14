import unittest
from circle import area,perimeter

class CircleTestCase(unittest.TestCase):
    def test_circle_area_norm(self):
        res = area(5)
        self.assertEqual(res, 78.540)

    def test_circle_area_neNorm(self):
        with self.assertEqual(ValueError):
            area(-6)
        
    def test_circle_area_real(self):
        res = area(5.5)
        self.assertEqual(res, 95.033)

    def test_circle_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_perimeter_norm(self):
        res = perimeter(5)
        self.assertEqual(res, 31.416)

    def test_circle_perimeter_neNorm(self):
        with self.assertEqual(ValueError):
            perimeter(-5)

    def test_circle_perimeter_real(self):
        res = perimeter(5.5)
        self.assertEqual(res, 34.558)

    def test_circle_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

if name == '__main__':
    unittest.main()
