list = ["1", "2", "3", "4"]

print(list)
a="uio"
def fun():
    # global a= "heyu" why not like this
    global a
    a="heyu"

fun()

print("hyu"+a)

x= b"Hello"
print(x)

y = bytearray(5)	#bytearray	
z = memoryview(bytes(5))	#memoryview	
w = None #None type
print(y)
print(z)
print(w)