import time
import math
# def powerfunc(x,n):
#     if n==1 or x==1:
#         return x
#     else:
#         return x*powerfunc(x,n-1)

# start =time.time()
# print(powerfunc(23000768009,34))
# end =time.time()
# print(end-start)

# efficient way

def power(x,n):
    global count 
    count+=1
    if n==1:
        return x
    if n==2:
        return x*x
    if n%2 == 0:
        return power(x,n/2)*power(x,n/2)
    else:
        return (power(x,int(n/2))*power(x,int(n/2)))*(x)
count=0
start = time.time()
print(power(12,30))
print(count)
end=time.time()
print(end-start)