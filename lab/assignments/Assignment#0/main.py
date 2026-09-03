print("Welcome!".center(100,'-'))
print("Choose your 3 favourite numbers that you would like to be compared:")
a= input("1st Number(a): ")
b= input("2nd Number(b): ")
c= input("3rd Number(c): ")
if a>=b:
    if a>=c:
        if a==b and b==c:
            print('a=b=c')
        elif b>=c:
            if a==b:
                print('a=b>c')
            elif b==c:
                print('a>b=c')
            else:
                print('a>b>c')
        else:
            if a==c:
                print('a=c>b')
            else:
                print('a>c>b')
    elif a==b:
        print('c>a=b')
    else:
        print('c>a>b')
elif a>=c:
    if a==c:
        print('b>a=c')
    else:
        print('b>a>c')
elif c>=b:
    if b==c:
        print('b=c>a')
    else:
        print('c>b>a')
else:
    print('b>c>a')

print('Thank You!'.center(100, '-'))
