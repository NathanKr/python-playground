msg = "hello"

def printMsg():
    print ("message is : " + msg)
    global g
    g = 999


printMsg()
print(g)