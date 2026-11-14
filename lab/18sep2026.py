import time
import math
# start = time.time()
# print("Hello World")
# end = time.time()
# print(end-start)
def isPrime(y):
    if y==1:
        return False
    if y==2:
        return True
    if y%2==0:
        return False
    for i in range(3, int(math.sqrt(y))+1, 2):
        if y%i==0:
            return False
    return True

# print(isPrime(11784579))

def prime_list(n):
    out =[]
    out.append(2)
    for i in range(3,n+1,2):
        if isPrime(i):
            out.append(i)
    return out


start = time.time()
print(prime_list(43))
end = time.time()
print(end-start)

def erastolist(n):
    ilist = [2,3,5]
    state = True
    while True:
        if ilist[len(ilist)-1]>n:
            break
        if state:
            ilist.append(ilist[len(ilist)-1]+2)
            state=False
        else:
            ilist.append(ilist[len(ilist)-1]+4)
            state=True
    ilist.pop()
    return ilist

print(erastolist(100))