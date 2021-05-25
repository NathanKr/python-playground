# mutable object   : 
#   - an object whos state CAN be updated after its creation
#   - e.g. containers like list,dict, set
# immutable object : 
#   - an object whos state can NOT be updated after its creation 
#   - e.g. primitives like string , number


# string is immuteable 
# thus on update a new object is created on new address which str_name point to
str_name = 'Nathan'
print(f'id(str_name) : {id(str_name)} , str_name : {str_name}')
str_name = 'Krasney'
print(f'id(str_name) : {id(str_name)} , str_name : {str_name}')

# list is mutable
# thus on update the same object and adderss is used
list = [1,2,3]
print(f'id(list) : {id(list)} , list : {list}')
list.append(4)
list[0]=11
print(f'id(list) : {id(list)} , list : {list}')








