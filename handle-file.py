import os 

file_path = os.path.join('data','a.txt')

# option 1 we need to close ourself 
file = open(file_path,'r') 
print(file.read())
file.close() 

# option 2 close is done implicitly
with open(file_path, 'r') as file: 
    print(file.read()) 


