# Quicksort Algorithm
import time, random
def partion(l, start, end):
    p=l[start]
    i=start+1
    j=end

    while (i<j):
        if (l[i]<p and l[j]>=p):
            i+=1
            j-=1
        elif(l[i]>=p and l[j]<p):
            l[i], l[j] = l[j], l[i]
            i+=1
            j-=1
        elif (l[i]<p and l[j]<p):
            i+=1
        elif(l[i]>=p and l[j]>=p):
            j-=1

    if j<i:
        l[j], l[start] = l[start], l[j]
        return j
    if i==j:
        if l[i]<p:
            l[i], l[start] = l[start], l[i]
            return i
        else:
            l[i-1], l[start] = l[start], l[i-1]
            return i-1


def quicksort(l, start, end):
    if end-start <1:
        return
    else:
        x= partion(l, start, end)
        quicksort(l, start, x-1)
        quicksort(l, x+1, end)


n = 10000
l=   random.sample(range(1, 10001), n)
length = len(l)
start = time.time()
quicksort(l, 0, length-1)
end = time.time()
for x in l:
    print(x, end=" ")

print(end-start)