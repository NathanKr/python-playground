def print_kwargs(**kwargs): 
    print (f'type(kwargs) : {type(kwargs)}')
    print(kwargs)


print_kwargs(num1=1,num2=2,num3=3)        

dict = {'num1':11,'num2':2,'num3':3}
print_kwargs(**dict)
