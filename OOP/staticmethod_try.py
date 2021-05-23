class Foo:
    def __init__(self, num1):
        self.num1 = num1

    @staticmethod
    def write_hello():
        print('Hello')


Foo.write_hello()