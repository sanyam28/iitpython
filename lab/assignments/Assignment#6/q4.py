import time,random

n=10000
def inplaceinsertionsort(l):
    
    for i in range(1,len(l)):
        insert_index = i
        value = l.pop(i)
        for j in range(i-1,-1,-1):
            if l[j]>value:
                insert_index=j
        l.insert(insert_index,value)
    return

l=random.sample(range(1, 10001), n)
start1 = time.time()
inplaceinsertionsort(l)
end1=time.time()
print("inplaceinsertsort",end1-start1)

def simplesort(l):
    smallest = l[0]
    j=0
    while j<=(len(l)-1):
        smallest = l[j]
        small_index = j
        for i in range(j+1,len(l)):
            if l[i]<smallest:
                smallest = l[i]
                small_index = i
        l[small_index], l[j]=l[j],l[small_index]
        j+=1
    return

li=random.sample(range(1, 10001), n)
start2 =time.time()
simplesort(li)
end2=time.time()
print("simplesort",end2-start2)


def mergesort(arr):
    if len(arr)<=1:
        return arr

    mid = len(arr)//2
    lefthalf = arr[:mid]
    righthalf = arr[mid:]

    sortedleft = mergesort(lefthalf)
    sortedright = mergesort(righthalf)

    return merge(sortedleft, sortedright)

def merge(sortedleft, sortedright):
    result = []
    i=0
    j=0

    while i<len(sortedleft) and j<len(sortedright):
        if sortedleft[i]<=sortedright[j]:
            result.append(sortedleft[i])
            i+=1
        else:
            result.append(sortedright[j])
            j+=1
    result.extend(sortedleft[i:])
    result.extend(sortedright[j:])
    return result

unsortedarr = random.sample(range(1, 10001), n)
time3=time.time()
sortedarr = mergesort(unsortedarr)
end3 = time.time()
print("mergesort", end3-time3)

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

li3 = random.sample(range(1, 10001), n)
length = len(li3)
start4 = time.time()
quicksort(li3, 0, length-1)
end4 = time.time()

print("quicksort", end4-start4)
