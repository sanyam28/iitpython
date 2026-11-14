# vertices and edges

class Node:
    def __init__(self, val):
        self.val =val

class Edge:
    def __init__(self,ori,dest):
        self.ori = ori
        self.dest = dest

class Graphs:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def addNode(self, node):
        if node in self.nodes:
            print("Node is already present")
            return
        else:
            self.nodes.append(node)
            self.edges[node] ={}

    def addEdge(self, edge):
        self.edges[edge.ori].append(edge.dest)

g =Graphs()
g.addNode(Node(34))
g.addNode(Node(45))
g.addNode(Node(34))
g.addNode(Node(65))
g.addNode(Node(12))
g.addNode(Node(356))
g.addNode(Node(33))





