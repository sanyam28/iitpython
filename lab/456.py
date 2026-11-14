class BST:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None
        self.head = root
        self.count = 1

    def insert(self,key):
        if self.head ==None:
            self.head = key
        if self.root == key:
            self.count +=1
            return
        elif self.root>key:
            if self.left ==None:
                self.left = BST(key)
            else:
                self.left.insert(key)
        else:
            if self.right ==None:
                self.right = BST(key)
            else:
                self.right.insert(key)

    def delete(self, key):
        arr = self.inorder()
        if key<arr[0] or key>arr[len(arr)-1]:
            return False
        if self.root == key:
            currentstate = self.right
            if currentstate is None:
                self.root = self.left.root
                self.left = self.left.left
                self.right = self.left.right
                self.count = self.left.count
                return True
            while True:
                if currentstate.left==None:
                    currentstate.left = self.left
                    break
                else:
                    currentstate = currentstate.left

            self.root = self.right.root
            self.left = self.right.left
            self.right = self.right.right
            self.count = self.right.count
            return True
        if self.left == None and self.right == None:
            return False
        if self.left is not None:
            if self.left.root == key:
                currentstate = self.left.left
                if currentstate ==None:
                    self.left = self.left.right
                    return True
                if self.left.right == None:
                    self.left = self.left.left
                    return True
                while True:
                    if currentstate.right==None:
                        currentstate.right = self.left.right
                        break
                    else:
                        currentstate = currentstate.right
                self.left = self.left.left
                return True
        if self.right is not None:
            if self.right.root == key:
                currentstate = self.right.right
                if currentstate ==None:
                    self.right = self.right.left
                    return True
                while True:
                    if currentstate.left==None:
                        currentstate.left = self.right.left
                        break
                    else:
                        currentstate = currentstate.left
                self.right = self.right.right
                return True
        if self.root>key:
            return self.left.delete(key)
        if self.root<key:
            return self.right.delete(key)

    def inorder(self, sor_arr=None):
        if sor_arr is None:
            sor_arr = []
        if self.left !=None:
            self.left.inorder(sor_arr)
        sor_arr.append(self.root)
        if self.right !=None:
            self.right.inorder(sor_arr)
        return(sor_arr)

    def balance(self):
        sorted_elements = self.inorder()
        def build(sarr, start, end):
            if start>end:
                return None
            mid = (start+end)//2
            b= BST(sarr[mid])
            b.left = build(sarr, start, mid-1)
            b.right = build(sarr, mid+1, end)
            return b
        b=build(sorted_elements, 0, len(sorted_elements)-1)
        self.root = b.root
        self.left = b.left
        self.right = b.right
        self.count = b.count

    def ceil(self, ref, headv = None, k=0):
        print(headv)
        if k==0:
            headv = self.root
            print(headv)
        k+=1
        if self.root == ref:
            if self.right == None:
                if self.root>headv:
                    return None
                else:
                    return headv
            return self.right.root
        elif self.root<ref:
            if self.right == None:
                return None
            return self.right.ceil(ref, headv, k)
        else:
            if self.left == None:
                return None
            return self.left.ceil(ref, headv, k)
    #     arr = self.inorder()
    #     for j in range(len(arr)):
    #         if arr[j]>ref:
    #             return arr[j]
    #     return None


arr = [23,34,45,22,19,46,1,3,2]
a=BST
def buildtree(x):
    global a
    a=BST(x[0])
    for i  in range(1, len(x)):
        a.insert(x[i])
buildtree(arr)

# a.balance()
print(a.inorder())
# print(a.delete(34))
# a.balance()
print(a.inorder())
print(a.ceil(4))