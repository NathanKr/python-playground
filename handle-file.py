import os 

file_path = os.path.join('data','a.txt')

# option 1 You need to close the handle and it 
# will not be called on exceptions
file = open(file_path,'r') 
print(file.read())
file.close() 

# option 2 Handle is closed implicitly  
# this is robust also against exceptions
with open(file_path, 'r') as file: 
    print(file.read()) 


