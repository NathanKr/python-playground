squares = []

# simple way
for num in range(10):
    squares.append(num**2)

print (squares)    

# use list comprehensions 
squares = [num**2 for num in range(10)]
print (squares)    