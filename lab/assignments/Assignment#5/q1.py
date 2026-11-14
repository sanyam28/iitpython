import math
import time
def factors(n):
    factors_list = []
    list2=[]
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            factors_list.append(i)
            list2.append(int(n/i))
    k = len(list2) -1
    while k>=0:
        if list2[k]!=factors_list[len(factors_list)-1]:
            factors_list.append(list2[k])
        k-=1
    return factors_list

start = time.time()
print("Factors of 89",factors(89))
end = time.time()
print(end-start)

def hcf(a,b):
    if b>a:
        a,b=b,a
    aFactors=factors(a)
    bFactors=factors(b)

    k= len(bFactors)-1
    while k>=0:
        for x in aFactors:
            if x==bFactors[k]:
                return x
        k-=1

start1 = time.time()
print(hcf(195000,200000))
end1 = time.time()
print(end1-start1)

def gcd(a,b):
    if a<b:
        a,b =b,a
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

start2 = time.time()
print(gcd(195000,200000))
end2 = time.time()
print(end2-start2)



