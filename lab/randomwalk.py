import random
import math

avg = 0


def dest(start, steps):
    x,y =start
    dir = [(1,0), (-1,0), (0,1), (0,-1)]
    for i in range(steps):
        a,b = random.choice(dir)
        x+=a
        y+=b
    return (x,y)


    
for i in range(100):
    x,y = (0,0)
    steps =2
    x2, y2 = dest((x,y), steps)
    avg+=math.sqrt((x2-x)**2 + (y2-y)**2)

print("average", avg/100)