

class Complete_BInary_Tree():

    def __init__(self,a, l):
        self.arr = a
        self.last = l

    # def parrentnode(self,);
    #      if self
    def li(self, i): # index of left child
        if (2*i +1)<=self.last:
            return 2*i +1
        else:
            return None
        
    def ri(self, i): # index of right child
        if (2*i +2)<=self.last:
            return 2*i +2
        else:
            return None

    def pi(self,i):
        if i==0:
            return -1
        else:
            return (self-1)//2
    
        

a = [4,2,1,11,18,19,10,3,40,30,6,5]
l= len(a) -1
tree1 = Complete_BInary_Tree(a,l)
