# Insert a value y after a given value x

l= [44,23,55,2,3,5,2,0]

def insert(l,last, x,y):
    # l.append(y)
    loc=-1
    # j =len(l)-2
    # while j >=0:
    #     if l[j] == x:
    #         break
    #     l[j], l[j+1] = l[j+1], l[j]
    #     j-=1
    for i in range(last+1):
        if l[i]==x:
            loc = i
            break
    if loc == -1:
        print(x, "not found")
        return
    else:
        last = last+1
        for i in range(last, loc+1, -1):
            l[i]= l[i-1]
    l[loc+1]=y

insert(l,6,2,456)
print(l)
