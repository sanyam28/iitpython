# from nicegui import ui
# ui.label("Hello World").label("h1")
# ui.run()

def gcd(a,b):
    global count
    count+=1
    if b>a:
        a,b = b,a

    if a%b ==0:
        return b
    else:
        return gcd(b,a%b)
count = 0
print(gcd(3400000,51))
print(count)

# Prime factors of a number

def isPrime(y):
    if y ==0 or y==1:
        return False
    if y==2:
        return True
    if y%2==0:
        return False
    for i in range(3, y, 2):
        if y%i==0:
            return False
    return True

def primefactors(x):
    pf= []
    for i in range(2, x):
        if x%i==0:
            if isPrime(i):
                pf.append(i)
    return pf

# print(primefactors(100))
print(isPrime(17))


