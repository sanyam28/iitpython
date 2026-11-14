
count=0
def mergesort(l,start,end):
    global count
    count+=1
    if end-start<=0:
        return
    else:
        mid = (start+end)//2
        mergesort(l, start, (start+end)//2)
        mergesort(l, (start+end)//2, end)
        merge(l,start, mid, end)


print(count)