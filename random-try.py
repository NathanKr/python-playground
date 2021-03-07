import random
list = [1,2,3,4,5,6]

random.shuffle(list)
print(list)

print("****** no seed : different list of random numbers")
for i in list:
    print(random.random())

random.seed(42)    
print("****** with seed : same list of random numbers")
for i in list:
    print(random.random())
