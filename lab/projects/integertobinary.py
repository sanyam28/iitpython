import time
def no_to_binary(n):

    quotient = n
    binaryno= ""
    while quotient>0:
        binaryno = str(quotient%2)+binaryno
        quotient = quotient//2

    return int(binaryno)

# print(no_to_binary(13))

def binary_to_no(binaryno):
    binaryno =str(binaryno)
    length = len(binaryno)
    number = 0
    k = length-1
    j=0
    while k>=0:
        number+=int(binaryno[k])*(2**(j))
        k-=1
        j+=1
    return number

# print(binary_to_no(1101))

def power(x,n):
    print(no_to_binary(n))
    bidi = str(no_to_binary(n))
    lengthv = len(bidi)
    power_seq = []
    for i in range(0, len(bidi)):
        if i==0:
            power_seq.append(x)
        else:
            power_seq.append(power_seq[i-1]*power_seq[i-1])
    print(bidi)
    print(power_seq)
    ans = 1
    k = len(bidi)-1
    while k>=0:
        if int(bidi[k])==1:
            ans*=power_seq[lengthv-1-k]
        k-=1
    return ans

start = time.time()
print(power(6,5))
end=time.time()
print(end-start)
