# Finding out square root of a number

# Exhaustive enumeration Method
a= float(input("Choose the number for which you want square root to be calculated: "))

if a<0:
    print('Square roots of negative numbers have no real existence.')
else:
    epsilion_init = 0.0001

    ans = 0
    iterations = 0

    while ans**2 <a:
        ans+=epsilion_init
        iterations+=1

    print('Square root of', a)
    print(ans)
    print('Number of iterations is: ', iterations)

# Efficient method - Bisection Search
x= float(input("Your no. "))
if x<0:
    print('Square roots of negative numbers have no real existence.')
else:
    lower_l = 0
    upper_l = 0
    if x>1:
        upper_l=x
    else:
        upper_l=1
    ans = (lower_l+upper_l)/2

    iterate_v = 0.00001
    no_of_iterations = 0

    while abs(ans**2 - x) >iterate_v:
        if (ans**2>x):
            upper_l = ans
        else:
            lower_l = ans
        ans =(upper_l+lower_l)/2
        no_of_iterations +=1

    print('Your square root is' ,ans)
    print('No of iterations:', no_of_iterations)