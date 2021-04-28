
from typing import List
def print1(num1 : int):
    print(num1)        

def sum(num1 : int , num2 : int)->int:
    return num1+num2        

print1("xyz")    #this will NOT cause an error
print1(1) # this is good

x: int = 0
l : List[str] = ["1" , 'a' , 'b']
