class Person:
    # first argument is
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def write(self):
        print("Name : {} , Age : {}".format(self.name,self.age))
