# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-21 16:16:33
# LastEditTime: 2023-12-21 16:26:18
# Description: 

class Shape:
    def draw(self):
        pass
        

class Rectangle(Shape):
    def draw(self):
        print("Inside Rectangle::draw() method.")

class Square(Shape):
    def draw(self):
        print("Inside Square::draw() method.")

class Circle(Shape):
    def draw(self):
        print("Inside Circle::draw() method.")

class ShapeFactory:
    def getShape(self, shape):
        if shape == 'Circle':
            return Circle()
        elif shape == 'Rectangle':
            return Rectangle()
        elif shape == 'Square':
            return Square()
            
factory = ShapeFactory()
a = factory.getShape('Circle')
a.draw()

b = factory.getShape('Rectangle')
b.draw()

c = factory.getShape('Square')
c.draw()
