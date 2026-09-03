def factorial(no):
    fac_calc = no
    for i in range(no):
        if i!=0:
            temp = fac_calc
            fac_calc = temp*(no-i)
    return fac_calc

user_inp = int(input('Choose the number for that factorial to be calculated: '))
result = factorial(user_inp)

print(result)