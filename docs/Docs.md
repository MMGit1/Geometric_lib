# Проект Geometric Lib
Проект содержит функции для высчитывания площади и периметра различных фигур - квадрата, прямоугольника, треугольника, круга. 

Функция Area принимает измерения фигуры в зависимости от того, какие нужны для вычисления её площади.
Пример использования в Triangle.py:
```
def area(a, h): 
    return a * h / 2 
# Принимает сторону и высоту к ней треугольника a и h и возвращает его площадь
def perimeter(a, b, c): 
    return a + b + c 
# Принимает три стороны треугольника a,b,c и возвращает его периметр
print(area(4, 3))
6.0
```
Функция perimeter принимает измерения фигуры в зависимости от того, какие нужны для вычисления её периметра.
Пример Использования в Circle.py:
```
import math
def area(r):
    return math.pi * r * r
# Принимает значение радиуса окружности r и возвращает площадь круга с таким радиусом 

def perimeter(r):
    return 2 * math.pi * r
#  Принимает значение радиуса окружности r и возвращает длину круга с таким радиусом
print(perimeter(10))
62.8
```
История работы над проектом:
```
8c2c696 (HEAD -> Main, origin/Main) error fixed
d3e9c96 New file added
92d6d62 new file added
c48d495 .
d078c8d L-03: Docs added
8ba9aeb L-03: Circle and square added
```