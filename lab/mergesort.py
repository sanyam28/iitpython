count1 = 0
count2 =0 

def mergesort(arr):
    global count1
    count1+=1
    if len(arr)<=1:
        return arr

    mid = len(arr)//2
    lefthalf = arr[:mid]
    righthalf = arr[mid:]

    sortedleft = mergesort(lefthalf)
    sortedright = mergesort(righthalf)

    return merge(sortedleft, sortedright)

def merge(sortedleft, sortedright):
    global count2
    result = []
    i=0
    j=0

    while i<len(sortedleft) and j<len(sortedright):
        count2+=1
        if sortedleft[i]<=sortedright[j]:
            result.append(sortedleft[i])
            i+=1
        else:
            result.append(sortedright[j])
            j+=1
    result.extend(sortedleft[i:])
    result.extend(sortedright[j:])
    return result

unsortedarr = [9,8,7,6,5,4,3,2]
sortedarr = mergesort(unsortedarr)
print(sortedarr)
print(count1,count2)
