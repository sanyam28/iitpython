

def cal_log(x, base):
    ans = x
    epsilon = 0.1
    count = 0
    while base**ans-x>=epsilon:
        ans = ans - epsilon
        count+=1
    print(count)

    return ans

a= int(input('Logarithmic Calculations, choose base: \n'))
b= int(input('choose number: \n'))
print(cal_log(b, a))