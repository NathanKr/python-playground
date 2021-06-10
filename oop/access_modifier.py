class Foo:

    def __init__(self,num1,num2):
        self.num1 = num1    # by default - public
        self.__num2 = num2  # __ mark as private

    @property
    def name(self):
       return self.__num2

obj = Foo(1,2)
# print(obj.__name) this is not allowed
print (obj.num1 , obj.name)
# obj.name = 2 this is not allowed