#Heaps
import random

# class Complete_Binary_Tree():
#     def __init__(self,a,l):
#         self.arr = a
#         self.last = l

#     def li(self,i):   #index of left child
#         if ((2*i)+1 <= self.last): 
#             return 2*i+1 
#         else:
#             return None
    
#     def ri(self,i):   #index of right child
#         if ((2*i)+2 <= self.last): 
#             return 2*i+2 
#         else:
#             return None
#     def pi(self,i):
#         if i == 0:
#             return None
#         else:
#             return i//2

#     def heapify(self,i):
#         largest = i
#         left = self.li(i)
#         right = self.ri(i)

#         if left != None and self.arr[left]>self.arr[largest]:
#             largest = left

#         if right != None and self.arr[right]>self.arr[largest]:
#             largest = right

#         if largest != i:
#             self.arr[i],self.arr[largest] = self.arr[largest],self.arr[i]
#             self.heapify(largest)

#     def build_heap(self):
#         for i in range((self.last-1)//2,-1,-1):
#             self.heapify(i)

#         return self.arr

# a = [4,2,1,11,18,19,10,3,40,30,6,5]
# l = len(a)-1
# tree1 = Complete_Binary_Tree(a,l)

# print((tree1.build_heap()))

# create an additional attribute to keep track count of repeated values inside class

class BST:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None


    def insert(self, key):
        if self.root == key:
            return
        elif self.root> key:
            if self.left==None:
              self.left = BST(key)
            else:
                self.left.insert(key)
        else:
            if self.right==None:
                self.right = BST(key)
            else:
                self.right.insert(key)

    def inorder(self,sortedlist):
        if self.left != None:
            self.left.inorder(sortedlist)
        sortedlist.append(self.root)
        if self.right != None:
            self.right.inorder(sortedlist)
        return sortedlist
    def search(self, key):
        if self.root == key:
            return True
        elif self.root>key:
            # if self.left:
            self.left.search(key)
        elif self.root<key and self.right!=None:
            self.right.search(key)
        else:
            return False

# inorder traversal
x = [23,34,45,75,4,5,73]
# x= random.sample(range(1,101), 20)
ad = BST(x[0])
sortedlist = []
for j in x:
    ad.insert(j)
print(x)
print(ad.search(23))

