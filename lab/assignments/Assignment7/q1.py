#Trees

class Complete_Binary_Tree():
    def __init__(self,a,l):
        self.arr = a
        self.last = l

    def li(self,i):   #index of left child
        if ((2*i)+1 <= self.last): 
            return 2*i+1 
        else:
            return None
    
    def ri(self,i):   #index of right child
        if ((2*i)+2 <= self.last): 
            return 2*i+2 
        else:
            return None
    def pi(self,i):
        if i == 0:
            return None
        else:
            return i//2

    def heapify(self,i):
        largest = i
        left = self.li(i)
        right = self.ri(i)

        if left != None and self.arr[left]>self.arr[largest]:
            largest = left

        if right != None and self.arr[right]>self.arr[largest]:
            largest = right

        if largest != i:
            self.arr[i],self.arr[largest] = self.arr[largest],self.arr[i]
            self.heapify(largest)

    def build_heap(self):
        for i in range((self.last-1)//2,-1,-1):
            self.heapify(i)

        return self.arr


a = [4,2,1,11,18,19,10,3,40,30,6,5]
l = len(a)-1
tree1 = Complete_Binary_Tree(a,l) 
print(tree1.build_heap())