def split(a,k):
    y = a%(10**k)
    x = (a-y)/(10**k)
    return int(x),int(y)

def di(a):
    k=1
    while True:
        if (a//(10**k))==0:
            break
        else:
            k+=1
    return k

total_m = 0
def karatsuba(a,b):
    global total_m
    if a-10<0 or b-10<0:
        if a-10<0 and b-10<0:
            total_m+=1
        else:
            total_m+=2
        return a*b
    else:
        k = (di(a) if di(a)<di(b) else di(b))//2
        a1, a0 = split(a,k)
        b1, b0 = split(b,k)
        m1 = karatsuba(a1, b1)
        m2 = karatsuba(a0,b0)
        m3 = karatsuba(a1+a0, b1+b0)
        m= (10**(2*k))*m1 + (10**k)*(m3-m1-m2) +m2
        return m

print(karatsuba(1111,11111))
print(total_m)