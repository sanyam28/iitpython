def no_to_binary(n):
    if n==0:
        return 0

    quotient = n
    binaryno= ""
    while quotient>0:
        binaryno = str(quotient%2)+binaryno
        quotient = quotient//2

    return int(binaryno)

# print('Number to Binary Conversion')
# notobinary = abs(int(input("Enter non negative integer: \n")))
# print(no_to_binary(notobinary))
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
# print('Binary to Number Conversion')
# binarytono = abs(int(input("Enter binary number: \n")))
# print(binary_to_no(binarytono))

def power_rec(x,n):
    if n==1:
        return x
    elif n==2:
        return x*x
    else:
        return x*power_rec(x, n-1)
print(power_rec(4,3))


def power(x,n):
    bidi = str(no_to_binary(n))
    lengthv = len(bidi)
    power_seq = []
    for i in range(0, len(bidi)):
        if i==0:
            power_seq.append(x)
        else:
            power_seq.append(power_seq[i-1]*power_seq[i-1])
    ans = 1
    k = len(bidi)-1
    while k>=0:
        if int(bidi[k])==1:
            ans*=power_seq[lengthv-1-k]
        k-=1
    return ans

print("Power calculation using binary conversion method")
base = 0
powerr = 0
while True:
    base = float(input("Choose Base: "))
    if base!=0:
        break
    else:
        print("Base should be other than zero")

powerr= abs(int(input("Choose non negative integer power: disclaimer: negative values will be considered as positive: ")))

    

print(power(base,powerr))
