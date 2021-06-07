from enum import Enum, auto , unique

@unique # this will assure that enum values are unique
class Color(Enum):
     RED = auto()
     GREEN = auto()
     BLUE = auto()


print(Color.RED)     
print(Color.RED == 1)     
print(Color['RED'] == Color.RED)
print(list(Color))

for color in Color:
     print(f'color : {color} , type(color) : {type(color)}')