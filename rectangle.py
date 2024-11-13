import unittest

def area(a,b):
    # Принимает длины двух смежных сторон прямоугольника, возвращает площадь прямоугольника.
    return a*b
def perimeter(a,b):
    # Принимает длины двух смежных сторон прямоугольника, возвращает периметр прямоугольника.
    return 2*(a+b)    

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        self.assertRaises(Exception, lambda:area(10,0))
        
    def test_square_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
        
    def test_negative_area(self):
        self.assertRaises(Exception, lambda:area(-1, 10))
        
    def test_zero_perimeter(self):
        self.assertRaises(Exception, lambda:perimeter(10,0))
        
    def test_negative_perimeter(self):
        self.assertRaises(Exception, lambda:perimeter(-2,2))
        
    def test_perimeter(self):
        res = perimeter(10, 2)
        self.assertEqual(res, 24)