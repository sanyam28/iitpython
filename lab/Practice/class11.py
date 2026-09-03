# Newton raphsilon technique

# Calculating square root of a number

x= int(input('Choose no>: '))
n=int(input('choose the value of n: '))
epsilon = 0.0000000000001
guess_t =0 

ans = x
slope =0 

if abs(x)>1:
    if x< 0 and n%2 == 0:
        print('when n is even, solution does not exist for negative numbers')

    else:
        while ans**n - x>epsilon:
            slope = (n)*(ans**(n-1))
            ans = ans - (ans**n-x)/slope
            guess_t+=1
        print(ans)
        print(guess_t)

else:
    print('yet to design')