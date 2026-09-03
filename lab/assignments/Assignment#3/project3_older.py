# Finding cube roots of a number
import matplotlib.pyplot as plt
import math
def nthroot(z,a):
    if z ==0:
        return z
    epsilon = 0.0001
    ans_n = z
    while abs(ans_n**a-z)>epsilon:
        ans_n = (ans_n + z/(ans_n**(a-1)))/2
    return ans_n

# golden ratio spiral

def createset(a,b, parts):
    set=[]
    for i in range(parts):
        set.append(a+((b-a)/parts)*i)

    return set


def fibo(alpha):
    n=alpha+1
    nfib = [0,1]
    for i in range(3,n+1):
        nfib.append(nfib[i-2]+nfib[i-3])
    return nfib[n-1]

origin = [0,0]

x_axis = []
y_axis = []
steps =1000

def get_curve_with_direction(radius, direc_no):
    if direc_no == 0:
        for i in createset(math.pi,3*math.pi/2,steps):
            vx = origin[0] + radius*math.cos(i)
            vy = origin[1] + radius*math.sin(i)
            x_axis.append(vx)
            y_axis.append(vy)
    elif direc_no == 1:
        for i in createset(-math.pi/2,0,steps):
            vx = origin[0] + radius*math.cos(i)
            vy = origin[1] + radius*math.sin(i)
            x_axis.append(vx)
            y_axis.append(vy)
    elif direc_no == 2:
        for i in createset(0, math.pi/2,steps):
            vx = origin[0] + radius*math.cos(i)
            vy = origin[1] + radius*math.sin(i)
            x_axis.append(vx)
            y_axis.append(vy)
    else:
        for i in createset(math.pi/2,math.pi,steps):
            vx = origin[0] + radius*math.cos(i)
            vy = origin[1] + radius*math.sin(i)
            x_axis.append(vx)
            y_axis.append(vy)

    # if direc_no == 0 or direc_no == 3:
    #     print('here')
    #     epsilon = 0.0001=
    #     j=0
    #     k = centre[0]-radius
    #     while j <= radius:
    #         x_axis.append(k)
    #         if(direc_no==3):
    #             y_axis.append(origin[1] + nthroot(radius**2-(radius-j)**2, 2))
    #         else:
    #             y_axis.append(origin[1] - nthroot(radius**2-(radius-j)**2, 2))
    #         k+=epsilon
    #         j+=epsilon
    # else:
    #     epsilon = 0.0001
    #     j=0
    #     k = centre[0]
    #     while j <= radius:
    #         x_axis.append(k)
    #         if(direc_no==2):
    #             y_axis.append(origin[1] + nthroot(radius**2-j**2, 2))
    #         else:
    #             y_axis.append(origin[1] - nthroot(radius**2-j**2, 2))
    #         k+=epsilon
    #         j+=epsilon

    return
            

for i in range(3,11):

    get_curve_with_direction(fibo(i), (i-3)%4)
    mod = (i-3)%4
    if(mod==0):
        origin[1]+= (fibo(i+1)-fibo(i))
    elif(mod==1):
        origin[0]-= (fibo(i+1)-fibo(i))
    elif(mod==2):
        origin[1]-= (fibo(i+1)-fibo(i))
    else:
        origin[0]+= (fibo(i+1)-fibo(i))

plt.plot(x_axis, y_axis)
plt.show()