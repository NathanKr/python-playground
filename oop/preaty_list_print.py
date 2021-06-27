from dataclasses import dataclass, field
from typing import List

@dataclass
class Foo:
    list : List = field(default_factory=list)

    def __str__(self)->str:
     s = ''
     i=0
     for item in self.list:
         s += f'\n{i+1}) {str(item)}'   
         i += 1
     
     return s


f = Foo(list = [1,2,3])
print(f)