class Foo:
    num2 = 22 # common to all objects

    def __init__(self, num1):
        self.num1 = num1

    def write(self):
        print(f'num1 : {self.num1} , num2 : {Foo.num2}')

    @classmethod
    def set_num2(cls,val):
        cls.num2 = val         

foo1 = Foo(11)
foo1.write()
Foo.set_num2(55)
foo1.write()
foo2 = Foo(33)
foo2.write()

