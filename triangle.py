import unittest

def area(a,h):
    # Принимает длину стороны треугольника и длину высоты, опущенной к этой стороне.
    # Возвращает площадь треугольника.
    return a*h/2
def perimeter(a,b,c):
    # Принимает длины трех сторон треугольника. Возвращает периметр треугольника.
    return a+b+c    

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        self.assertRaises(Exception, lambda:area(10,0))
        
    def test_area(self):
        res = area(10, 10)
        self.assertEqual(res, 50)
        
    def test_negative_area(self):
        self.assertRaises(Exception, lambda:area(-1, 10))
        
    def test_zero_perimeter(self):
        self.assertRaises(Exception, lambda:perimeter(10,0,2))
        
    def test_negative_perimeter(self):
        self.assertRaises(Exception, lambda:perimeter(-2,2,7))
    
    def test_triangle_inequality_perimeter(self):
        self.assertRaises(Exception, lambda:perimeter(2,3,30))    
        
    def test_perimeter(self):
        res = perimeter(3,4 ,5 )
        self.assertEqual(res, 12)