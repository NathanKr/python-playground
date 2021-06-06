from dataclasses import dataclass


@dataclass
class Rectangle:
    width:int
    height:int

    def compute_area(self)->int:
        return self.width * self.height # self out of the box for width,height  

# out of the box __init__ with width , height as data members
obj1 = Rectangle(10,20)
obj2 = Rectangle(100,200)
obj3 = Rectangle(10,20)

print(obj1 == obj2) # out of the box == operator
print(obj1 == obj3)
print(obj1.compute_area())
