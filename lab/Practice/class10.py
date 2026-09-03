# Finding cube roots of a number
x= int(input("Enter the no. for its cube root: "))
i=0
ans = x
epsilon = 0.0001
iteration = 0
# while abs(ans**3 - x)>epsilon:
#     ans = (ans + (x)/(ans**2))/2
#     iteration+=1
# print(ans)
# print(iteration)

# lets find nth root of a number

print('Lets find nth root of a number')
a= int(input('Select the value of n: '))
z= int(input('select the no.: '))

ans_n = z
guess = 0

if(a%2==0 and z<0):
    print('for n even, negative no does have real solutions.')

else:
    while abs(ans_n**a-z)>epsilon:
        ans_n = (ans_n + z/(ans_n**(a-1)))/2
        guess+=1

print(ans_n)
print(guess)