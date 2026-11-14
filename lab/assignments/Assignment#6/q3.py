import random
def inplaceinsertionsort(l):
    
    for i in range(1,len(l)):
        insert_index = i
        value = l.pop(i)
        for j in range(i-1,-1,-1):
            if l[j]>value:
                insert_index=j
        l.insert(insert_index,value)
    return

l=[45,32, 98,32,43,104,1003,1,2,3,4,56,33,23,323,5,3,2,5,7,8,5,3,2,5,67,7,5,3,2,4,6,7,7,5,3,2,2,345,5,234,97]
inplaceinsertionsort(l)
print("in place insert sort",l)

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

li=[45,32, 98,32,43,104,1003,1,2,3,4,56,33,23,323,5,3,2,5,7,8,5,3,2,5,67,7,5,3,2,4,6,7,7,5,3,2,2,345,5,234,97]
simplesort(li)
print("simplesort",li)

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

unsortedarr = random.sample(range(1, 31), 10)
sortedarr = mergesort(unsortedarr)
print("mergesort",sortedarr)