# *args can be useful when you do not know how many arguments you have
def print_args(*args): 
    print (f'type(args) : {type(args)}')
    for item in args:
        print(item)


print_args(1,2,3)        