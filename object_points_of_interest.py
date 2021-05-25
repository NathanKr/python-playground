a = 123
b = 321
c = 123
print(f'id(a) : {id(a)}\nid(b) : {id(b)}\nid(c) : {id(c)}\n')
c = c + 1
print(f'id(c) : {id(c)}\n')

s=""
for i in range(3):
    s += str(i)
    print(f's : {s} , id(s) : {id(s)}')

list=[]
for i in range(3):
    list.append(i)
    print(f'list : {list} , id(list) : {id(list)}')

