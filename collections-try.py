# list
mylist = ["apple", "banana", "cherry"]
print(mylist)
print(mylist[0])
for it in mylist:
     print(it)

# tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[0]) # print apple

(a, b, c) = thistuple # unpack tuple
print("a,b,c : ",a,b,c)

# set
myset = {3,4,5}
print (myset)
for it in myset:
    print(it)

# dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])