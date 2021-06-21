class Foo:
    num1 : int
    num2 : int


foo1 = Foo()
id_foo1_before = id(foo1)
foo1.num1 = 1
id_foo1_after = id(foo1)
if id_foo1_before == id_foo1_after:
    print('Foo is mutable')
else:
    print('Foo is immutable')        

