class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self,val):
        self.first = Node(val)

    def insert(self, node, x, y):
        if node.val == x:
            newNode = Node(y)
            newNode.next = node.next
            node.next = newNode
            return
        elif node.next == None:
            print(x, "not found")
            return
        else:
            return self.insert(node.next, x, y)
        
        



    