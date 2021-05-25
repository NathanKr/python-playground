def increment(x):
    print(f'address of x before increment : {id(x)}')
    x = x + 1
    print(f'x : {x}')
    print(f'address of x after increment  : {id(x)}')

n = 7
print(f'address of n : {id(n)}')
increment(n)
print(f'address of n : {id(n)}')
print(f'n : {n}')