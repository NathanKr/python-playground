l = [1,2,3,4,5]
print(l)

def mul_by2(num):
    return num*2

for result in map(mul_by2,l):
    print(result)
