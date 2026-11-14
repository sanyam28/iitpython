# Tower of Hanoi
steps=0
def hanoi(n,a,b,c):
    global steps
    if n==1:
        steps+=1
        print("Disk from", a, "to", b)
        return
    else:
        hanoi(n-1,a,c,b)
        steps+=1
        print("Disk from", a, "to",b)
        hanoi(n-1,c,b,a)

hanoi(5,"a", "b","c")
print(steps)