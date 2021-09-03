
## Abstraction
In software Engineering,  abstraction means the act of hiding irrelevant classes from users to reduce complexity. This means that users can create some functions without worrying about how they work. They know what the function does but they don't need to know the logic behind it. Let me give you an example, let's look at our smartphones for instance we can use the camera to take pictures, but we don't the operations that are happening in the background while taking the picture.

In Python, we can achieve abstraction by using abstract classes and interfaces. You may be wondering what is an abstract class?  It's any class that contains at least one abstract method and cannot be instantiated, but can be subclassed. An abstract class is useful when designing large functions and it also provides large interfaces for the implementation of components. Let's create an abstraction in python using the abc module. 

## code
```
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
```

## Output
```
Triangle has 3 sides
This is a normal class
Square has 4 sides
This is a normal class

```
## Explaination
We created the abstract base class Shape using the ABC module that was import from Python, and also created an abstract method sides(). The Triangle() and Square() classes inherited the base class  and have their own side() methods. The  were created and the sides() methods was invoked, The sides() methods, hidden definitions were activated when the user creates the Triangle() and Square() objects and invoked the sides() method. The sides() method defined in the Shape() class in never invoked, while the normal() method is invoked because is not an abstract method.


## Conclusion
Abstraction is important whenever we want to hide core functionalities from users.  An abstract class can contain both a normal method and an abstract method. We noticed that abstract method in the abstract class are never activated while the normal method was activated.
