from abc import ABC, abstractmethod


class Shape(ABC):
    # abstract method
    @abstractmethod
    def sides(self):
        print('This is the main class')

    def normal(self):
        print('This is a normal class')


class Triangle(Shape):
    def sides(self):
        print(' Triangle has 3 sides')


class Square(Shape):
    def sides(self):
        print(' Square has 4 sides')


t = Triangle()
t.sides()
t.normal()

s = Square()
s.sides()
s.normal()