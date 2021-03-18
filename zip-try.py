fruits = ["orange" , "banana" , "melon"]
cars = ["ford" , "bmw" , "fiat"]
numbers = [11,32,21]

# OK
i=0
while i < len(fruits):
    print(fruits[i],cars[i],numbers[i])
    i += 1

# much better
for f,c,n in zip(fruits,cars,numbers):
    print(f,c,n)

# this is also possible    
for t in zip(fruits,cars,numbers):
    print(t) # t is a tuple
